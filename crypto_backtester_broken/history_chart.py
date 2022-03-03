import pathlib
import json
from datetime import datetime, timedelta
from itertools import count

import pandas
import yfinance as yf
from reflect import (
    Controller,
    Mapping,
    js,
    make_observable,
    memoize,
    get_window,
)
from reflect_ant_icons import MinusCircleFilled, PlusCircleFilled
from reflect_antd import (
    AutoComplete,
    Button,
    Col,
    DatePicker,
    InputNumber,
    Row,
    Select,
    Switch,
    Typography,
)
from reflect_html import div, label
from reflect_plotly import Plot

DEFAULT_TICKER = "AAPL"
CANDLE_STICK_NAME = "candlestick"
OHLC_NAME = "ohlc"
MESSAGE_KEY = "key"


def create_form_item(label_tag, component):
    return Row(
        [
            Col(
                label(label_tag),
                span=8,
                className="ant-form-item-label",
            ),
            Col(
                component,
                span=16,
                className="ant-form-item-control-input-content",
            ),
        ],
        style=dict(marginTop=10),
    )


class App:
    def __init__(self, ticker=None):
        today = datetime.today()
        self.controller = Controller()
        records = json.loads(
            open(
                pathlib.Path(__file__).parent.joinpath("nasdaq/nasdaq.json").resolve(),
                "r",
            ).read()
        )["data"]["table"]["rows"]
        tickers = {record["symbol"]: record["name"] for record in records}
        self.ticker_autocomplete = AutoComplete(
            options=[{"value": name} for name in tickers],
            defaultValue=ticker or DEFAULT_TICKER,
            style=dict(textAlign="right", width=200),
            filterOption=js("autoCompleteFilterOption"),
            backfill=True,
        )

        def full_name():
            return tickers.get(self.ticker_autocomplete(), "")

        range = DatePicker.RangePicker(
            defaultValue=[today - timedelta(days=365), today]
        )
        range_slider = Switch(defaultChecked=True)
        graph_type = Select(
            defaultValue=CANDLE_STICK_NAME,
            options=[
                dict(label="Candles", value=CANDLE_STICK_NAME),
                dict(label="OHLC", value=OHLC_NAME),
            ],
            style=dict(width=200),
        )
        self.header = [
            Typography.Title(full_name, level=5, style=dict(marginLeft=15)),
            create_form_item("Ticker", self.ticker_autocomplete),
            create_form_item("Range", range),
            create_form_item("Graph type", graph_type),
            create_form_item("Range slider", range_slider),
        ]
        signal_definitions = make_observable(
            [],
            depth=3,
            key="signal_definitions",
            controller=self.controller,
        )
        signal_counter = count(1)

        def create_signal_settings_component(values):
            return Row(
                [
                    Col(
                        label(
                            f"Signal {next(signal_counter)}",
                        ),
                        span=8,
                        className="ant-form-item-label",
                    ),
                    Col(
                        Row(
                            [
                                Col(span=4),
                                Col(
                                    InputNumber(
                                        value=values["nb_days"],
                                        style=dict(width=80, textAlign="right"),
                                    ),
                                    span=6,
                                ),
                                Col(
                                    Select(
                                        [
                                            Select.Option("Blue", value="blue"),
                                            Select.Option("Red", value="red"),
                                            Select.Option("Green", value="green"),
                                            Select.Option("Yellow", value="yellow"),
                                        ],
                                        value=values["color"],
                                        style=dict(width=80, textAlign="right"),
                                    ),
                                    span=6,
                                ),
                                Col(
                                    Button(
                                        MinusCircleFilled(),
                                        onClick=lambda: signal_definitions.remove(
                                            values
                                        ),
                                    )
                                ),
                            ]
                        ),
                        span=16,
                        className="ant-form-item-control-input-content",
                    ),
                ],
                style=dict(marginTop=10),
            )

        self.signals_settings = Mapping(
            create_signal_settings_component,
            signal_definitions,
            depth=2,
            key="signals_settings",
        )
        self.signal_labels = Row(
            [
                Col(span=8),
                Col(
                    Row(
                        [
                            Col(span=4),
                            Col(
                                label("nb days :"),
                                span=6,
                            ),
                        ]
                    ),
                    span=16,
                ),
            ]
        )
        self.add_signal_row = Row(
            [
                Col(
                    Button(
                        [PlusCircleFilled(), "Add signal"],
                        type="dashed",
                        onClick=lambda: signal_definitions.append(
                            {"nb_days": 2, "color": "red"}
                        ),
                    ),
                    span=8,
                    className="ant-form-item-label",
                ),
                Col(
                    span=16,
                ),
            ],
            style=dict(marginTop=10),
        )

        @memoize()
        def fetch_data() -> pandas.DataFrame:
            ticker, [start, end] = self.ticker_autocomplete(), range()
            if True:
                result = yf.download(
                    ticker,
                    start=start.strftime("%Y-%m-%d"),
                    end=end.strftime("%Y-%m-%d"),
                )
                # open("demos/yahoo_ticks.pick", "wb").write(pickle.dumps(result))
            else:
                import pickle

                result = pickle.loads(open("demos/yahoo_ticks.pick", "rb").read())
            return result

        @memoize()
        def abscissa():
            return pandas.Series(d.strftime("%Y-%m-%d") for d in fetch_data().index)

        @memoize(controller=self.controller)
        def generate_signal(settings):
            df = fetch_data()
            nb = settings["nb_days"]()
            return {
                "name": f"Mv Avg {nb} days",
                "type": "scatter",
                "line": {"color": settings["color"]()},
                "x": abscissa(),
                "y": df.Close.rolling(nb).mean(),
            }

        signals = Mapping(
            generate_signal, signal_definitions, depth=1, controller=self.controller
        )
        signal_definitions.append({"nb_days": 2, "color": "red"})

        @memoize(controller=self.controller)
        def data():
            df = fetch_data()
            history = {
                "x": abscissa(),
                "decreasing": {"line": {"color": "cyan"}},
                "increasing": {"line": {"color": "gray"}},
                "type": graph_type(),
                "xaxis": "x",
                "yaxis": "y",
                "name": "Daily changes",
            }
            history.update(
                {name.lower(): df[name] for name in ["Open", "Close", "Low", "High"]}
            )
            return [history] + list(signals())

        def layout():
            return {
                "dragmode": "zoom",
                "margin": {"r": 20, "t": 25, "b": 40, "l": 60},
                "showlegend": False,
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

        self.content = Plot(
            data=data,
            layout=layout,
            config=dict(responsive=True),
            useResizeHandler=True,
            style={
                "width": "100%",
                "marginRight": 60,  # the graph looks at the right location when the icons are hidden...
            },
        )

    def settings(self):
        return Col(
            [
                self.header,
                self.add_signal_row,
                self.signal_labels,
                self.signals_settings,
            ]
        )

    def ok(self):
        self.controller.commit()

    def cancel(self):
        self.controller.revert()

    def title(self):
        return self.ticker_autocomplete.evaluate() or DEFAULT_TICKER


def content(ticker):
    app = App(ticker)
    return {
        name: getattr(app, name)
        for name in ["title", "settings", "content", "ok", "cancel"]
    }


def app(ticker=DEFAULT_TICKER):
    app = App(ticker)
    get_window().set_title(app.title)
    return div(
        [
            Col(
                [
                    app.settings,
                    Row(
                        [
                            Button(
                                "Update",
                                type="primary",
                                onClick=app.ok,
                                style=dict(margin=15),
                            ),
                            Button(
                                "Revert",
                                type="primary",
                                onClick=app.cancel,
                                style=dict(margin=15),
                            ),
                        ],
                        align="center",
                    ),
                ],
                style={"marginLeft": 15},
                key="settings",
            ),
            app.content,
        ],
        style={"width": "600", "height": "400", "marginTop": 20},
    )
