"""Fetch historical data from yahoo in real time, plot time series and signals using plotly."""

import datetime
import io
import json
import pathlib

import httpx
import pandas as pd
import render as r
import render_antd as antd
import render_html as html
import render_plotly as plotly

CANDLE_STICK_NAME = "candlestick"
OHLC_NAME = "ohlc"
MESSAGE_KEY = "key"
YAHOO_URL = "https://query1.finance.yahoo.com/v8/finance/chart/"
TICKERS_PATH = "stock_prices/nasdaq/nasdaq.json"
DEFAULT_SIGNAL_DEFINITION = {"nb_days": 2, "color": "red"}


def signal_name(settings_obs):
    nb_days = settings_obs["nb_days"]
    return "" if nb_days is None else f"MVA {nb_days()}"


def create_row_settings(elements):
    return antd.Row(
        [
            antd.Col(element, span=span)
            for element, span in zip(elements, [5, 4, 10, 5])
        ],
        align="middle",
        style={"height": "100%", "marginTop": 10},
        gutter={"xs": 8, "sm": 16, "md": 24, "lg": 32},
    )


filter_options = r.js_arrow(
    "filter",
    "(inputValue, {value}) => value.toUpperCase().indexOf(inputValue.toUpperCase()) !== -1",
)


class App:
    def __init__(self, window: r.Window, ticker, stand_alone=True):
        today = datetime.datetime.today()
        self.title = ticker
        self.controller = r.Controller()
        tickers = {
            record["symbol"]: record["name"]
            for record in json.loads(
                pathlib.Path(__file__).parent.parent.joinpath(TICKERS_PATH).read_text()
            )["data"]["table"]["rows"]
        }
        self.ticker_autocomplete = antd.AutoComplete(
            options=[{"value": ticker} for ticker in tickers],
            value=ticker,
            style={"textAlign": "right", "width": 100},
            filterOption=filter_options,
            allowClear=True,
        )
        start_date = antd.DatePicker(defaultValue=today - datetime.timedelta(days=365))
        end_date = antd.DatePicker(defaultValue=today)
        graph_type = antd.Select(
            defaultValue=CANDLE_STICK_NAME,
            options=[
                {"label": "Candles", "value": CANDLE_STICK_NAME},
                {"label": "OHLC", "value": OHLC_NAME},
            ],
            style={"width": 100},
        )
        range_slider = antd.Switch(defaultChecked=True)
        show_legends = antd.Switch(defaultChecked=True)
        self.header = antd.create_form_layout(
            [
                ("Ticker", self.ticker_autocomplete),
                ("Start", start_date),
                ("End", end_date),
                ("Graph type", graph_type),
                ("Range slider", range_slider),
                ("Show legends", show_legends),
            ]
        )
        with self.controller:
            self.signal_definitions = [DEFAULT_SIGNAL_DEFINITION.copy()]
            self.signal_definitions_obs = r.ObservableList(
                self.signal_definitions, key="signal_definitions_obs"
            )
            self.signal_definitions_obs_obs = r.Mapping(
                lambda x: r.DictOfObservables(x, controller=self.controller),
                self.signal_definitions_obs,
            )
            self.signals_settings = r.Mapping(
                self.create_signal_settings_row,
                self.signal_definitions_obs_obs,
                key="signals_settings",
                evaluate_argument=False,
            )
        self.signal_setting_labels = create_row_settings(
            [
                None,
                html.label("days"),
                html.label("color"),
                antd.Button(
                    "+",
                    onClick=lambda: self.signal_definitions_obs.append(
                        DEFAULT_SIGNAL_DEFINITION.copy()
                    ),
                ),
            ]
        )
        yahoo_data = r.ObservableValue(pd.DataFrame(), key="yahoo_data")

        async def update_yahoo_data_async():
            print("Updating yahoo data")
            if not self.ticker_autocomplete():
                return
            start, end = start_date(), end_date()
            url = f"{YAHOO_URL}{self.ticker_autocomplete()}?period1={int(start.timestamp())}&period2={int(end.timestamp())}&interval=1d&events=history"
            async with httpx.AsyncClient(headers={"User-Agent": "Mozilla/5.0"}) as client:
                try:
                    data = await client.get(url)
                except Exception as exception:
                    raise RuntimeError(
                        f"Failed to retrieve data from yahoo: {exception}"
                    ) from exception
                if data.status_code != 200:
                    raise RuntimeError(
                        f"Failed to retrieve data from yahoo: {data.status_code} {data.text}"
                    )
                result = json.loads(data.content.decode())["chart"]["result"][0]
                yahoo_data.set(pd.DataFrame({"x": result["timestamp"], **result["indicators"]["quote"][0]}))

        r.autorun(update_yahoo_data_async)

        def compute_signal(settings: r.DictOfObservables):
            df = yahoo_data()
            if df.empty:
                return {}
            return {
                "name": signal_name(settings),
                "type": "scatter",
                "line": {"color": settings["color"]()},
                "x": df.x,
                "y": df.close.rolling(settings["nb_days"]()).mean(),
            }

        signals_obs = r.Mapping(
            compute_signal,
            self.signal_definitions_obs_obs,
            key="signal_obs",
            evaluate_argument=False,
        )

        def chart_data():
            df = yahoo_data()
            if df.empty:
                return
            history = {
                "decreasing": {"line": {"color": "cyan"}},
                "increasing": {"line": {"color": "gray"}},
                "type": graph_type(),
                "xaxis": "x",
                "yaxis": "y",
                "name": "Daily changes",
                **df.to_dict(orient="list"),
            }
            return [history] + list(signals_obs())

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
                "yaxis": {"autorange": True, "domain": [0, 1], "type": "linear"},
                "autosize": True,
            }

        plot = plotly.Plot(
            data=chart_data,
            layout=layout,
            config={"responsive": True},
            useResizeHandler=True,
            style={
                "height": "var(min(100%, 0.5 * vh))" if stand_alone else "100%",
                "width": "100%",
                "marginRight": 60,
            },
        )
        title = antd.Typography.Title(
            lambda: tickers.get(self.ticker_autocomplete(), ""),
            level=5,
            style=lambda: {
                "textAlign": "center",
                "margin": r.ResponsiveValue(0, md=16)(),
            },
        )
        self.content = html.div(
            [title, plot] if stand_alone else [plot], style={"height": "100%"}
        )

    def create_signal_settings_row(self, settings: r.DictOfObservables):
        with self.controller:
            return create_row_settings(
                [
                    html.label(
                        lambda: signal_name(settings), style={"textAlign": "right"}
                    ),
                    antd.InputNumber(
                        value=settings["nb_days"], style={"width": "100%"}
                    ),
                    antd.Select(
                        options=[
                            {"children": "Blue", "value": "blue"},
                            {"children": "Red", "value": "red"},
                            {"children": "Green", "value": "green"},
                            {"children": "Yellow", "value": "yellow"},
                        ],
                        value=settings["color"],
                        style={"width": "100%", "textAlign": "right", "maxWidth": 80},
                    ),
                    antd.Button(
                        "-",
                        onClick=lambda: self.signal_definitions_obs.remove(settings),
                        style={"width": 42},
                    ),
                ]
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

    def update(self):
        self.controller.commit()


def content(ticker, stand_alone=True):
    app = App(ticker, stand_alone)
    return {
        name: getattr(app, name)
        for name in ["title", "settings", "content", "ok", "cancel"]
    }


def app(window: r.Window):
    # TODO: use window.hash to store the ticker
    ticker = r.ObservableValue("AAPL", key="ticker")
    app = App(window, ticker)
    window.set_title(app.title)
    return antd.Row(
        [
            antd.Col(
                [
                    app.settings,
                    antd.Divider(),
                    antd.Row(
                        antd.Col(
                            antd.Button("Update", type="primary", onClick=app.update),
                        ),
                        justify="center",
                    ),
                ],
                key="settings",
                xs=24,
                md=12,
                style={"maxWidth": 500},
            ),
            antd.Col(app.content, xs=24, md=12, style={"maxWidth": 500}),
        ],
        justify="center",
        style={"padding": 5, "width": "100%"},
    )
