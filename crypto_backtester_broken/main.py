import datetime
import pickle
from itertools import chain, count
from typing import Optional
import json

import altair as alt
import anyio
import pandas as pd
import py_vollib_vectorized
from py_vollib.black_scholes.implied_volatility import implied_volatility
from reflect import get_window, js, memoize
from reflect import autorun, make_observable
from reflect_altair import Chart
from reflect_antd import Col, Select
from reflect_html import div
from reflect_utils.common import ws_connection_manager
from .utils import PendingResult, to_timestamp
import websockets

Option = Select.Option

URI = "wss://test.deribit.com/ws/api/v2"
GREEN = "#57A44C"
BLUE = "#5276A7"
RED = "#FF0000"
TITLE = "Option backtester"


def create_performance_chart(
    derebit_data,
    currency_data: pd.DataFrame,
    strike: Optional[float],
    expiry,
    r,
    option_type,
):
    if derebit_data.shape[0]:
        df = pd.DataFrame(
            {name: derebit_data[name] for name in ["close_option", "volume_option"]}
        )
        df["ticks"] = pd.Series(int(value.timestamp()) for value in derebit_data["ticks"])
    else:
        df = pd.DataFrame(
            {
                "volume": pd.Series(dtype="float64"),
                "ticks": pd.Series(dtype="<M8[ns]"),
                "close": pd.Series(dtype="float64"),
                "underlying": pd.Series(dtype="float64"),
            }
        )
    currency_data["ticks"] = pd.Series(int(datetime.datetime.strptime(value, "%m/%d/%Y").timestamp()) for value in currency_data["ticks"])
    currency_data["close_spot"] = currency_data["Close"]

    df = pd.merge(
        df,
        currency_data,
        how="left",
        on=["ticks"],
    )
    df["ticks"] = [datetime.datetime.fromtimestamp(tick / 1000) for tick in df["ticks"]]
    df["ivol_mid"] = implied_volatility(
        df["close_option"],
        df["close_spot"],
        strike,
        df.ticks.apply(lambda x: (expiry - x).days / 365),
        r,
        option_type,
        return_as="series",
    )
    axis = alt.Axis(
        format="%d/%m",
        labelAngle=-45,
        title=None,
    )
    base = (
        alt.Chart(df)
        .mark_line()
        .transform_fold(
            ["close_spot", "close_option", "ivol_mid"],
            as_=["Measure", "Value"],
        )
        .encode(
            alt.Color("Measure:N", legend=None),
            alt.X("ticks:T", axis=axis),
        )
    )
    underlying = base.transform_filter(alt.datum.Measure == "close_spot").encode(
        alt.Y("Value:Q", axis=alt.Axis(title=None), scale=alt.Scale(zero=False)),
    )
    instrument = base.transform_filter(alt.datum.Measure == "close_option").encode(
        alt.Y("Value:Q", axis=alt.Axis(title=None), scale=alt.Scale(zero=False)),
    )
    if strike:
        underlying = underlying + (
            alt.Chart(pd.DataFrame({"y": [strike]}))
            .mark_rule(strokeDash=[10, 10])
            .encode(y="y")
        )
    ivol_mid = base.transform_filter(alt.datum.Measure == "ivol_mid").encode(
        alt.Y("Value:Q", axis=alt.Axis(title=None), scale=alt.Scale(zero=False)),
    )
    volume = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            alt.X("ticks:T", axis=axis),
            y="volume",
        )
    )
    return alt.vconcat(
        *[
            alt.layer(*encodings)
            .resolve_scale(y="independent")
            .interactive()
            .properties(height="container", width="container")
            for encodings in [(underlying, instrument), (volume, ivol_mid)]
        ]
    )


class App:
    def __init__(self, window):
        self.window = window
        self.request_id = count()
        self.pending_queries = {}
        self.connection_ready = anyio.Event()
        instruments = pd.DataFrame(
            chain.from_iterable(
                pickle.loads(open(f"{ccy}_instruments.pick", "rb").read())
                for ccy in ["BTC", "ETH"]
            )
        )
        select_style = dict(width=120, paddingTop=10)
        currency = Select(
            [
                Option("Bit Coin", value="BTC"),
                Option("Etherum", value="ETH"),
            ],
            defaultValue="BTC",
            style=select_style,
        )

        @memoize()
        def instrument_for_ccy():
            return instruments[instruments["base_currency"] == currency()]

        @memoize()
        def expiry_timestamp():
            return Select(
                [
                    Option(
                        datetime.datetime.fromtimestamp(value / 1000).strftime(
                            "%d/%m/%y"
                        ),
                        value=value,
                    )
                    for value in sorted(
                        set(instrument_for_ccy()["expiration_timestamp"])
                    )
                ],
                style=select_style,
            )

        @memoize()
        def instruments_for_expiry():
            return instrument_for_ccy()[
                instrument_for_ccy()["expiration_timestamp"] == expiry_timestamp()()
            ]

        @memoize()
        def option_type():
            return Select(
                [
                    Option(value, value=value)
                    for value in sorted(set(instruments_for_expiry()["option_type"]))
                ],
                style=select_style,
            )

        @memoize()
        def instruments_for_expiry_and_type():
            return instruments_for_expiry()[
                instruments_for_expiry()["option_type"] == option_type()()
            ]

        @memoize()
        def strike():
            return Select(
                [
                    Option(value, value=value)
                    for value in sorted(
                        set(instruments_for_expiry_and_type()["strike"])
                    )
                ],
                style=select_style,
            )

        side_bar = Col(
            [currency, expiry_timestamp], #option_type, strike],
            style={"backgroundColor": "red", "width": 200, "textAlign": "center"},
        )

        @memoize()
        def selected_instrument():
            if strike()():
                selected_instruments = instruments_for_expiry_and_type()[
                    instruments_for_expiry_and_type()["strike"] == strike()()
                ]
                assert selected_instruments.shape[0] == 1
                return selected_instruments.iloc[0]["instrument_name"]

        chart_data = make_observable(None)

        async def update_chart_data():
            if selected_instrument():
                instrument = await self.create_instrument_chart(
                    selected_instrument(),
                    datetime(2020, 9, 23),
                    datetime(2021, 10, 23),
                    "1D",
                )
                print(instrument)

        def test():
            print(selected_instrument())
        autorun(test)

        def chart():
            currency_data = pickle.loads(open(f"{currency()}.pick", "rb").read())
            if strike()() or True:
                instrument_name = "BTC-24JUN22-30000-C"
                derebit_data = pickle.loads(
                    open(f"{instrument_name}.pick", "rb").read()
                )
            else:
                derebit_data = None
            chart = create_performance_chart(
                derebit_data,
                currency_data,
                50000.0,
                datetime.datetime(2022, 6, 24),
                0.01,
                "c",
            )
            chart = Chart(
                chart,
                style={
                    # magic numbers to get altair.vconcat to dimension charts correctly (responsiveness is broken as charts size incread by a factor of two...)
                    "height": "42.5%",
                    "width": "95%",
                },
            )
            return div(
                chart,
                style={"height": "100%", "flexGrow": 1, "backgroundColor": "green"},
            )

        self.root = div(
            [chart, side_bar],
            style=dict(
                position="absolute",
                height="100%",
                width="100%",
                display="flex",
                flexFlow="row",
            ),
        )
        window.start_soon(self.main)
        window.start_soon(self.process_client_messages)

    async def get_currency_data(self, currency, start, end, resolution):
        return await self.query_derebit(
            "get_tradingview_chart_data",
            {
                "instrument_name": currency + "-PERPETUAL",
                "start_timestamp": to_timestamp(start),
                "end_timestamp": to_timestamp(end),
                "resolution": resolution,
            },
        )

    async def create_instrument_chart(self, instrument_name, start, end, resolution):
        instrument_data = await self.query_derebit(
            "get_tradingview_chart_data",
            {
                "instrument_name": instrument_name,
                "start_timestamp": to_timestamp(start),
                "end_timestamp": to_timestamp(end),
                "resolution": resolution,
            },
        )
        underlying_data = await self.get_currency_data(
            instrument_name[:3], start, end, resolution
        )
        import pickle

        open(f"{instrument_name[:3]}.pick", "wb").write(pickle.dumps(underlying_data))
        open(f"{instrument_name}.pick", "wb").write(pickle.dumps(instrument_data))
        await self.dock_layout.insert_component(
            instrument_name,
            Chart(
                create_performance_chart(instrument_data, underlying_data).properties(
                    width="container", height="container"
                )
            ),
        )

    async def process_client_messages(self):
        await self.connection_ready.wait()
        async for code, args in self.window.client_connection:
            if code == "historical_chart":
                for instrument_name in args:
                    await self.create_instrument_chart(
                        instrument_name,
                        datetime(2020, 9, 23),
                        datetime(2021, 10, 23),
                        "1D",
                    )
            if code == "order_book":
                for instrument_name in args:
                    await self.get_order_book(instrument_name, 10)

    async def main(self):
        while True:
            try:
                connection_manager = ws_connection_manager(
                    uri=URI,
                    task_group=self.window.task_group,
                    dumps=json.dumps,
                    loads=json.loads,
                    number_messages=False,
                )
                async with connection_manager as self.derebit_connection:
                    self.connection_ready.set()
                    async for response in self.derebit_connection:
                        if "id" in response:
                            is_error = "error" in response
                            self.pending_queries.pop(response["id"]).set(
                                response["error" if is_error else "result"], is_error
                            )
                        else:
                            print(response)
            except websockets.exceptions.ConnectionClosedError:
                print("Derebit connection has been reset, looping...")

    async def query_derebit(self, method, params={}):
        request_id = next(self.request_id)
        await self.derebit_connection.send(
            dict(
                jsonrpc="2.0",
                id=request_id,
                method="public/" + method,
                params=params,
            )
        )
        pending_result = self.pending_queries[request_id] = PendingResult()
        return await pending_result.wait()


def app():
    window = get_window()
    app = App(window)
    return app.root
