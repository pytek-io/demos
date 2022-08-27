"""Fetch historical data from yahoo in real time, plot time series and signals using plotly."""
import io
import json
import pathlib
from datetime import datetime, timedelta

import httpx
import pandas
from reflect import (
    Controller,
    WindowSize,
    autorun,
    create_mapping,
    get_window,
    js,
    create_observable,
    memoize,
    ResponsiveValue,
)
from reflect_antd import (
    AutoComplete,
    Button,
    Col,
    DatePicker,
    Divider,
    InputNumber,
    Row,
    Select,
    Space,
    Switch,
    Typography,
)
from reflect_html import div, label
from reflect_plotly import Plot
from reflect_utils.antd import create_form_row, LEFT_BREAK_POINTS, RIGHT_BREAK_POINTS

DEFAULT_TICKER = "AAPL"
CANDLE_STICK_NAME = "candlestick"
OHLC_NAME = "ohlc"
MESSAGE_KEY = "key"

COLOR_WIDTH = 90
NB_DAYS_WIDTH = 90
YAHOO_URL = "https://query1.finance.yahoo.com/v7/finance/download/"


def signal_name(settings):
    nb_days = settings["nb_days"]
    return "" if nb_days is None else f"MVA {settings['nb_days']()}"


class App:
    def __init__(self, ticker=None, stand_alone=True):
        today = datetime.today()
        self.controller = Controller()
        records = json.loads(
            open(
                pathlib.Path(__file__)
                .parent.parent.joinpath("stock_prices/nasdaq/nasdaq.json")
                .resolve(),
                "r",
            ).read()
        )["data"]["table"]["rows"]
        tickers = {record["symbol"]: record["name"] for record in records}
        self.ticker_autocomplete = AutoComplete(
            options=[{"value": name} for name in tickers],
            defaultValue=ticker or DEFAULT_TICKER,
            style=dict(textAlign="right", width=100),
            filterOption=js("autoCompleteFilterOption"),
            backfill=True,
        )

        def full_name():
            return tickers.get(self.ticker_autocomplete(), "")

        start_date = DatePicker(defaultValue=today - timedelta(days=365))
        end_date = DatePicker(defaultValue=today)
        graph_type = Select(
            defaultValue=CANDLE_STICK_NAME,
            options=[
                dict(label="Candles", value=CANDLE_STICK_NAME),
                dict(label="OHLC", value=OHLC_NAME),
            ],
            style=dict(width=100),
        )
        range_slider = Switch(defaultChecked=True)
        show_legends = Switch(defaultChecked=True)
        self.header = [
            create_form_row("Ticker", self.ticker_autocomplete),
            create_form_row("Start", start_date),
            create_form_row("End", end_date),
            create_form_row("Graph type", graph_type),
            create_form_row("Range slider", range_slider),
            create_form_row("Show legends", show_legends),
        ]
        signal_definitions = create_observable(
            [{"nb_days": 2, "color": "red"}],
            depth=3,
            key="signal_definitions",
            controller=self.controller,
        )

        def create_signal_settings_component(settings):
            return Row(
                [
                    Col(
                        # we add a lambda to avoid recomputing the whole row when the number of days changes (this causes the focus to be lost on mobiles)
                        label(lambda: signal_name(settings)),
                        className="ant-form-item-label",
                        **LEFT_BREAK_POINTS,
                    ),
                    Col(
                        Space(
                            [
                                InputNumber(
                                    value=settings["nb_days"],
                                    style=dict(width=NB_DAYS_WIDTH),
                                ),
                                Select(
                                    [
                                        Select.Option("Blue", value="blue"),
                                        Select.Option("Red", value="red"),
                                        Select.Option("Green", value="green"),
                                        Select.Option("Yellow", value="yellow"),
                                    ],
                                    value=settings["color"],
                                    style=dict(width=COLOR_WIDTH, textAlign="right"),
                                ),
                                Button(
                                    "-",
                                    onClick=lambda: signal_definitions.remove(settings),
                                    style=dict(width=42),
                                ),
                            ],
                        ),
                        **RIGHT_BREAK_POINTS,
                    ),
                ],
                style=dict(marginTop=10),
            )

        self.signals_settings = create_mapping(
            create_signal_settings_component,
            signal_definitions,
            key="signals_settings",
            controller=self.controller,
            evaluate_argument=False,
        )
        self.signal_setting_labels = Row(
            [
                Col(**LEFT_BREAK_POINTS),
                Col(
                    Space(
                        [
                            div(
                                "days",
                                style=dict(
                                    width=NB_DAYS_WIDTH,
                                    textAlign="center",
                                ),
                            ),
                            div(
                                "color",
                                style=dict(
                                    width=COLOR_WIDTH,
                                    textAlign="center",
                                ),
                            ),
                            Button(
                                "+",
                                onClick=lambda: signal_definitions.append(
                                    {"nb_days": 2, "color": "red"}
                                ),
                                style=dict(
                                    width=42, textAlign="center", marginRight=10
                                ),
                            ),
                        ],
                    ),
                    **RIGHT_BREAK_POINTS,
                ),
            ],
        )

        yahoo_data = create_observable(pandas.DataFrame())

        async def fetch_data_async():
            start, end = start_date(), end_date()
            url = f"{YAHOO_URL}{self.ticker_autocomplete()}?period1={int(start.timestamp())}&period2={int(end.timestamp())}&interval=1d&events=history"
            async with httpx.AsyncClient() as client:
                try:
                    data = await client.get(url)
                except Exception as exception:
                    raise RuntimeError(
                        f"Failed to retrieve data from yahoo: {exception}"
                    ) from exception
                yahoo_data.set(pandas.read_csv(io.BytesIO(data.content)))

        autorun(fetch_data_async, controller=self.controller)

        def generate_signal(settings):
            df = yahoo_data()
            return {
                "name": signal_name(settings),
                "type": "scatter",
                "line": {"color": settings["color"]()},
                "x": df.Date,
                "y": df.Close.rolling(settings["nb_days"]()).mean(),
            }

        signals = create_mapping(
            generate_signal,
            signal_definitions,
            "signal_definitions",
            evaluate_argument=False,
        )

        def data():
            df = yahoo_data()
            if not df.empty:
                history = {
                    "x": df.Date,
                    "decreasing": {"line": {"color": "cyan"}},
                    "increasing": {"line": {"color": "gray"}},
                    "type": graph_type(),
                    "xaxis": "x",
                    "yaxis": "y",
                    "name": "Daily changes",
                }
                history.update(
                    {
                        name.lower(): df[name]
                        for name in ["Open", "Close", "Low", "High"]
                    }
                )
                return [history] + list(signals())

        def layout():
            return {
                "dragmode": "zoom",
                "margin": {"r": 20, "t": 25, "b": 40, "l": 60},
                "showlegend": show_legends(),
                "xaxis": {
                    "autorange": True,
                    "domain": [0, 1],
                    "rangeslider": {"visible": range_slider()},
                    "type": "date",
                },
                "yaxis": {
                    "autorange": True,
                    "domain": [0, 1],
                    "type": "linear",
                },
                "autosize": True,
            }

        plot = Plot(
            data=data,
            layout=layout,
            config=dict(responsive=True),
            useResizeHandler=True,
            style={
                "height": "var(min(100%, 0.5 * vh))" if stand_alone else "100%",
                "width": "100%",
                "marginRight": 60,  # the graph looks at the right location when the icons are hidden...
            },
        )
        title = Typography.Title(
            full_name,
            level=5,
            style=lambda: {
                "textAlign": "center",
                "margin": ResponsiveValue(0, md=16)(),
            },
        )
        self.content = div(
            [title, plot] if stand_alone else [plot],
            style={"height": "100%"},
        )

        @memoize(controller=self.controller)
        def title():
            return self.ticker_autocomplete.evaluate() or DEFAULT_TICKER

        self.title = title

    def settings(self):
        return Col(
            [
                Divider("Time series"),
                self.header,
                Divider("Signals"),
                self.signal_setting_labels,
                self.signals_settings,
            ],
            controller=self.controller,
        )

    def ok(self):
        self.controller.commit()

    def cancel(self):
        self.controller.revert()


def content(ticker, stand_alone=True):
    app = App(ticker, stand_alone)
    return {
        name: getattr(app, name)
        for name in ["title", "settings", "content", "ok", "cancel"]
    }


def app(ticker=DEFAULT_TICKER):
    app = App(ticker)
    window = get_window()
    window.set_title(app.title)
    return Row(
        [
            Col(
                [
                    app.settings,
                    Divider(),
                    Row(
                        Col(
                            Space(
                                [
                                    Button(
                                        "Revert",
                                        type="primary",
                                        onClick=app.cancel,
                                    ),
                                    Button(
                                        "Update",
                                        type="primary",
                                        onClick=app.ok,
                                    ),
                                ],
                                style={
                                    "marginTop": 20,
                                    "marginBottom": 20,
                                },
                            )
                        ),
                        justify="center",
                    ),
                ],
                key="settings",
                xs=24,
                md=12,
            ),
            Col(app.content, xs=24, md=12),
        ],
        style=lambda: {"marginTop": "10vh" if window.size() >= WindowSize.md else None},
    )
