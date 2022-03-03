import datetime
import json
from datetime import datetime
from itertools import chain, count
import pickle

import altair as alt
import anyio
import pandas as pd
import websockets
from reflect import get_window, js
from reflect_aggrid import AgGridColumn, AgGridReact
from reflect_altair import Chart
from reflect_antd import Menu
from reflect_html import div
from reflect_rcdock import DockLayoutReflect
from reflect_utils.common import ws_connection_manager
from reflect_utils.md_parsing import parse_md_doc

from .config import COLUMNS, Column
from .utils import PendingResult, from_timestamp, to_timestamp


SESSION_MENU_ITEMS = [
    dict(name="History chart", action_tag="historical_chart"),
    dict(name="Order book", action_tag="order_book"),
]
URI = "wss://test.deribit.com/ws/api/v2"
GREEN = "#57A44C"
BLUE = "#5276A7"
RED = "#FF0000"
TITLE = "Option backtester"


def create_ag_grid_column(column: Column):
    return AgGridColumn(
        headerName=column.header_name,
        field=column.field,
        valueFormatter=column.formatter,
        sortingOrder=column.sorting_order,
        width=column.width,
        type=column.type,
        children=[create_ag_grid_column(child) for child in column.children],
    )


def dataframe_to_ag_grid(df, id_name):
    columns_as_list = list(df.columns)
    relevant_fields = [
        (columns_as_list.index(column.field), column.field, column.preprocess)
        for column in chain(
            COLUMNS, chain.from_iterable(col.children for col in COLUMNS)
        )
        if column.field
    ]
    id_name = None
    rowData = [
        {
            field: preprocess(record[index]) if preprocess else record[index]
            for index, field, preprocess in relevant_fields
        }
        for record in map(tuple, df.to_records(index=False))
    ]
    return AgGridReact(
        [create_ag_grid_column(column) for column in COLUMNS],
        rowData=rowData,
        rowHeight=24,
        defaultColDef=dict(resizable=True, filter=True, sortable=True),
        getContextMenuItems=js("createContextMenu", SESSION_MENU_ITEMS),
        getRowNodeId=js("fetch_attribute", id_name),
    )


def get_currency_historical_data(currency):
    result = pd.read_csv(
        f"demos/crypto_backtester/HistoricalData_{currency}.csv", index_col=False
    )
    return result.rename(columns={"Close/Last": "Close", "Date": "ticks"})


def create_performance_chart(derebit_data, currency_data):
    df = pd.DataFrame(derebit_data)
    df["ticks"] = [from_timestamp(tick) for tick in df.ticks]
    df = pd.merge(
        df,
        currency_data,
        how="left",
        on=["ticks"],
    )
    base = alt.Chart(df).encode(
        alt.X(
            "ticks:T",
            axis=alt.Axis(
                format="%d/%m",
                labelAngle=-45,
                title=None,
            ),
        )
    )
    underlying = base.mark_line(stroke=BLUE).encode(
        alt.Y("Close", axis=alt.Axis(title=None))
    )
    instrument = base.mark_line(stroke=GREEN, interpolate="step-after").encode(
        alt.Y("close", axis=alt.Axis(title="Instrument", titleColor=GREEN))
    )
    return (underlying + instrument).resolve_scale(y="independent").interactive()


class App:
    def __init__(self, window):
        self.window = window
        self.request_id = count()
        self.pending_queries = {}
        self.connection_ready = anyio.Event()
        welcome_panel = parse_md_doc(
            open("demos/crypto_backtester/welcome.md", "r").read()
        )
        defaultLayout = {
            "dockbox": {
                "mode": "vertical",
                "children": [
                    {
                        "tabs": [
                            dict(
                                content=welcome_panel,
                                title="Get started",
                                closeable=False,  # rmk this is not closeable as dock manager enters an invalid state (from our end at least) when it is empty
                            )
                        ],
                    },
                ],
            }
        }
        self.dock_layout = DockLayoutReflect(
            window,
            defaultLayout=defaultLayout,
            style={
                "position": "absolute",
                "left": 0,
                "top": 50,
                "right": 0,
                "bottom": 0,
            },
        )

        menu = Menu(
            [
                Menu.SubMenu(
                    [
                        Menu.ItemGroup(
                            [
                                Menu.Item(
                                    "BTC",
                                    onClick=lambda: self.display_instruments("BTC", "option"),
                                ),
                                Menu.Item(
                                    "ETH",
                                    onClick=lambda: self.display_instruments("ETH", "option"),
                                ),
                            ],
                            title="Instruments",
                        ),
                        Menu.ItemGroup(
                            [
                                Menu.Item(
                                    "BTC",
                                    onClick=lambda: self.display_currency_chart("BTC"),
                                ),
                                Menu.Item(
                                    "ETH",
                                    onClick=lambda: self.display_currency_chart("ETH"),
                                ),
                            ],
                            title="Currencies",
                        ),
                    ]
                ),
            ]
        )
        self.root = div([menu, self.dock_layout])

    async def display_instruments(self, currency, kind=None, expired=False):
        grid = None

        async def fetch_data():
            params = {"currency": currency, "expired": expired}
            if kind:
                params["kind"] = kind
            instruments = await self.query_derebit("get_instruments", params)
            open(f"{currency}_instruments.pick", "wb").write(pickle.dumps(instruments))
            await grid.applyTransactionAsync({"add": instruments})

        grid = AgGridReact(
            [create_ag_grid_column(column) for column in COLUMNS],
            rowData=[],
            rowHeight=24,
            defaultColDef=dict(resizable=True, filter=True, sortable=True),
            getContextMenuItems=js("createContextMenu", SESSION_MENU_ITEMS),
            getRowNodeId=js("fetch_attribute", "instrument_name"),
            componentDidMount=fetch_data,
        )
        await self.dock_layout.insert_component(
            f"{currency} {kind or 'instrument'}s", grid, className="ag-theme-balham"
        )

    async def display_currency_chart(self, currency):
        source = get_currency_historical_data(currency)
        base = alt.Chart(source).encode(
            alt.X(
                "ticks:T",
                axis=alt.Axis(
                    format="%m/%y" if source.shape[0] > 180 else "%d/%m",
                    labelAngle=-45,
                    title=None,
                ),
            ),
            color=alt.condition(
                "datum.Open <= datum.Close", alt.value("#06982d"), alt.value("#ae1325")
            ),
        )
        rule = base.mark_rule().encode(
            alt.Y(
                "Low:Q",
                title="Price",
                scale=alt.Scale(zero=False),
            ),
            alt.Y2("High:Q"),
        )
        bar = base.mark_bar().encode(alt.Y("Open:Q"), alt.Y2("Close:Q"))
        await self.dock_layout.insert_component(
            currency,
            Chart(
                (rule + bar)
                .interactive()
                .properties(width="container", height="container")
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

    async def get_currencies(self):
        print(await self.query_derebit("get_currencies"))

    async def get_order_book(self, instrument_name, depth=None):
        params = dict(instrument_name=instrument_name)
        if depth:
            params[depth] = depth
        print(await self.query_derebit("get_order_book", params))

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
        underlying_data = await self.get_currency_data(instrument_name[:3], start, end, resolution)
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

    async def subscribe(self):
        await self.query_derebit(
            "subscribe", {"channels": ["deribit_price_index.btc_usd"]}
        )


async def app():
    window = get_window()
    app = App(window)
    window.start_soon(app.main)
    window.start_soon(app.process_client_messages)

    async def test():
        await anyio.sleep(1.0)
        await app.create_instrument_chart(
            "BTC-24JUN22-30000-C", datetime(2020, 9, 23), datetime(2021, 10, 23), "1D"
        )

    # window.start_soon(test)
    return app.root
