"""Fetch historical data from yahoo in real time, plot time series and signals using plotly."""
import datetime
import io
import json
import pathlib

import httpx
import pandas as pd
import reflect as r
import reflect_antd as antd
import reflect_html as html
import reflect_plotly as plotly

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
    def __init__(self, ticker, stand_alone=True):
        if not ticker():
            ticker.set(DEFAULT_TICKER)
        today = datetime.datetime.today()
        self.title = ticker
        self.controller = r.Controller()
        records = json.loads(
            open(
                pathlib.Path(__file__)
                .parent.parent.joinpath("stock_prices/nasdaq/nasdaq.json")
                .resolve(),
                "r",
            ).read()
        )["data"]["table"]["rows"]
        tickers = {record["symbol"]: record["name"] for record in records}
        self.ticker_autocomplete = antd.AutoComplete(
            options=[{"value": name} for name in tickers],
            value=ticker,
            style=dict(textAlign="right", width=100),
            filterOption=r.js("autoCompleteFilterOption"),
            backfill=True,
        )

        def full_name():
            return tickers.get(self.ticker_autocomplete(), "")

        start_date = antd.DatePicker(defaultValue=today - datetime.timedelta(days=365))
        end_date = antd.DatePicker(defaultValue=today)
        graph_type = antd.Select(
            defaultValue=CANDLE_STICK_NAME,
            options=[
                dict(label="Candles", value=CANDLE_STICK_NAME),
                dict(label="OHLC", value=OHLC_NAME),
            ],
            style=dict(width=100),
        )
        range_slider = antd.Switch(defaultChecked=True)
        show_legends = antd.Switch(defaultChecked=True)
        self.header = [
            (antd.create_form_row(label, component))
            for label, component in [
                ("Ticker", self.ticker_autocomplete),
                ("Start", start_date),
                ("End", end_date),
                ("Graph type", graph_type),
                ("Range slider", range_slider),
                ("Show legends", show_legends),
            ]
        ]
        signal_definitions = r.create_observable(
            [{"nb_days": 2, "color": "red"}],
            depth=3,
            key="signal_definitions",
            controller=self.controller,
        )

        def create_signal_settings_component(settings):
            return antd.Row(
                [
                    antd.Col(
                        # we add a lambda to avoid recomputing the whole row when the number of days changes (this causes the focus to be lost on mobiles)
                        html.label(lambda: signal_name(settings)),
                        className="ant-form-item-html.label",
                        **antd.LEFT_BREAK_POINTS,
                    ),
                    antd.Col(
                        antd.Space(
                            [
                                antd.InputNumber(
                                    value=settings["nb_days"],
                                    style=dict(width=NB_DAYS_WIDTH),
                                ),
                                antd.Select(
                                    [
                                        antd.Select.Option("Blue", value="blue"),
                                        antd.Select.Option("Red", value="red"),
                                        antd.Select.Option("Green", value="green"),
                                        antd.Select.Option("Yellow", value="yellow"),
                                    ],
                                    value=settings["color"],
                                    style=dict(width=COLOR_WIDTH, textAlign="right"),
                                ),
                                antd.Button(
                                    "-",
                                    onClick=lambda: signal_definitions.remove(settings),
                                    style=dict(width=42),
                                ),
                            ],
                        ),
                        **antd.RIGHT_BREAK_POINTS,
                    ),
                ],
                style=dict(marginTop=10),
            )

        self.signals_settings = r.create_mapping(
            create_signal_settings_component,
            signal_definitions,
            key="signals_settings",
            controller=self.controller,
            evaluate_argument=False,
        )
        self.signal_setting_labels = antd.Row(
            [
                antd.Col(**antd.LEFT_BREAK_POINTS),
                antd.Col(
                    antd.Space(
                        [
                            html.div(
                                "days",
                                style=dict(
                                    width=NB_DAYS_WIDTH,
                                    textAlign="center",
                                ),
                            ),
                            html.div(
                                "color",
                                style=dict(
                                    width=COLOR_WIDTH,
                                    textAlign="center",
                                ),
                            ),
                            antd.Button(
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
                    **antd.RIGHT_BREAK_POINTS,
                ),
            ],
        )

        yahoo_data = r.create_observable(pd.DataFrame())

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
                yahoo_data.set(pd.read_csv(io.BytesIO(data.content)))

        r.autorun(fetch_data_async)

        def generate_signal(settings):
            df = yahoo_data()
            return {
                "name": signal_name(settings),
                "type": "scatter",
                "line": {"color": settings["color"]()},
                "x": df.Date,
                "y": df.Close.rolling(settings["nb_days"]()).mean(),
            }

        signals = r.create_mapping(
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

        plot = plotly.Plot(
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
        title = antd.Typography.Title(
            full_name,
            level=5,
            style=lambda: {
                "textAlign": "center",
                "margin": r.ResponsiveValue(0, md=16)(),
            },
        )
        self.content = html.div(
            [title, plot] if stand_alone else [plot],
            style={"height": "100%"},
        )

    def settings(self):
        return antd.Col(
            [
                antd.Divider("Time series"),
                self.header,
                antd.Divider("Signals"),
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


def app(window: r.Window):
    app = App(window.hash)
    window.set_title(app.title)
    return antd.Row(
        [
            antd.Col(
                [
                    app.settings,
                    antd.Divider(),
                    antd.Row(
                        antd.Col(
                            antd.Space(
                                [
                                    antd.Button(
                                        "Revert",
                                        type="primary",
                                        onClick=app.cancel,
                                    ),
                                    antd.Button(
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
            antd.Col(app.content, xs=24, md=12),
        ],
        style=lambda: {"marginTop": "10vh", "padding": "5vw"}
        if window.size() >= r.WindowSize.md
        else None,
    )
