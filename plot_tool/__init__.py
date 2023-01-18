"""Fetch historical data from yahoo in real time, plot time series and signals using plotly."""
import datetime
import itertools
import pathlib

import pandas as pd
import reflect as r
import reflect_antd as antd
import reflect_html as html
import reflect_monaco as monaco
import reflect_plotly as plotly
import reflect_ant_icons as ant_icons

from ..fred import get_fred_series_observations, get_yahoo_stock_history
from ..utils import merge_dicts
from .common import TimeSeries

ROOT = pathlib.Path(__file__).parent.parent
YAHOO_DATA = pd.read_pickle(ROOT.joinpath("stock_prices/nasdaq/nasdaq.pick"))
FRED_DATA = pd.read_pickle(ROOT.joinpath("fred.pick"))
YAHOO_TICKERS = dict(zip(YAHOO_DATA["symbol"], YAHOO_DATA["name"]))
FRED_TICKERS = dict(zip(FRED_DATA["id"], FRED_DATA["title"]))
EDITOR_OPTIONS = {
    "minimap": {"enabled": False},
    "lineNumbers": False,
    "glyphMargin": False,
    "wordWrap": False,
    "renderValidationDecorations": "off" if False else "on",
}
WIDTHS = [42, 100, 150, 80, 300]
TITLES = ["Source", "Ticker", "Name", "Description"]
YAHOO = "yahoo"
FRED = "fred"


def layout_timeseries_definition_row(elements, widths=WIDTHS, gap=10, justify="left"):
    return antd.Row(
        [
            antd.Col(element, style={"width": width, "marginRight": gap})
            for element, width in zip(elements, widths)
        ],
        align="middle",
        style={"height": "100%", "marginTop": 4},
        justify=justify,
    )


def input_panel(signal_definitions_obs):
    signal_count = itertools.count(1)
    add_signal = lambda: signal_definitions_obs.append(
        {"ticker": "AAPL", "name": f"input_{next(signal_count)}", "source": YAHOO}
    )
    # adding two values to make the example more user friendly
    add_signal()
    signal_definitions_obs.append(
        {
            "ticker": next(iter(FRED_TICKERS)),
            "name": f"input_{next(signal_count)}",
            "source": FRED,
        }
    )

    def create_timeseries_row(signal_obs_dict: r.DictOfObservables):
        tickers = (
            lambda: YAHOO_TICKERS
            if signal_obs_dict["source"]() == YAHOO
            else FRED_TICKERS
        )
        ticker = antd.AutoComplete(
            options=lambda: [{"value": ticker} for ticker in tickers()],
            value=signal_obs_dict["ticker"],
            style={"textAlign": "right", "width": "100%"},
            filterOption=antd.AutoComplete.case_insensitive_filter_options(),
            allowClear=True,
        )
        return layout_timeseries_definition_row(
            [
                antd.Button(
                    "-",
                    onClick=lambda: signal_definitions_obs.remove(signal_obs_dict),
                    style={"width": "100%"},
                ),
                antd.Select(
                    value=signal_obs_dict["source"],
                    options=[{"value": YAHOO}, {"value": FRED}],
                    style={"width": "100%"},
                    onChange=lambda _: ticker.set(None),
                ),
                ticker,
                antd.Input(value=signal_obs_dict["name"], style={"width": "100%"}),
                antd.Typography(lambda: tickers().get(ticker(), "Unknown time series")),
            ]
        )

    return antd.Col(
        [
            layout_timeseries_definition_row(
                [antd.Button("+", onClick=add_signal, style={"width": "100%"})]
                + [antd.Typography.Title(title, level=5) for title in TITLES]
            ),
            r.Mapping(create_timeseries_row, signal_definitions_obs),
        ],
    )


def plot_panel(editor, signal_definitions_obs):
    today = datetime.datetime.today()
    range_slider = antd.Switch(defaultChecked=False, style={"width": 30})
    show_legends = antd.Switch(defaultChecked=False, style={"width": 30})
    start_date = antd.DatePicker(defaultValue=today - datetime.timedelta(days=365))
    end_date = antd.DatePicker(defaultValue=today)
    chart_data = r.ObservableValue({})

    def fetch_timeseries(signal_definition):
        ticker = signal_definition["ticker"]()
        start, end = start_date(), end_date()
        if signal_definition["source"]() == YAHOO:
            data, tickers = get_yahoo_stock_history(ticker, start, end), YAHOO_TICKERS
        else:
            data, tickers = (
                get_fred_series_observations(ticker, start, end),
                FRED_TICKERS,
            )
        assert not data.empty, f"no data found for {ticker}"
        return signal_definition["name"](), TimeSeries(
            ticker, tickers.get(ticker), data
        )

    async def evaluate_script():
        scripts_locals = merge_dicts(locals(), dict(stock_timeseries))
        exec(await editor.getValue(), None, scripts_locals)
        chart_data.set(scripts_locals["figure"].to_dict())

    stock_timeseries = r.Mapping(fetch_timeseries, signal_definitions_obs)
    update = antd.Button(
        ["Update", ant_icons.ReloadOutlined()], onClick=evaluate_script, type="primary"
    )
    settings = antd.Col(
        [
            layout_timeseries_definition_row(
                [
                    html.label("Start"),
                    start_date,
                    html.label("End"),
                    end_date,
                    html.label("Range slider"),
                    range_slider,
                    html.label("Show legends"),
                    show_legends,
                ],
                [40, 140] * 2 + [100, 60] * 2,
                2,
            ),
        ]
    )

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

    return (
        settings,
        update,
        plotly.Plot(
            data=lambda: chart_data().get("data"),
            layout=lambda: merge_dicts(layout(), chart_data().get("layout", {})),
            style={"width": "100%"},
        ),
    )


def app(_: r.Window):
    signal_definitions_obs = r.ObservableList[r.DictOfObservables]()
    inputs = input_panel(signal_definitions_obs)
    editor = monaco.Editor(
        defaultValue=ROOT.joinpath("plot_tool", "script.py").read_text(),
        height=500,
        options=EDITOR_OPTIONS,
    )
    settings, update, plot = plot_panel(editor, signal_definitions_obs)
    framed_editor = html.div(
        editor,
        style={
            "marginTop": 40,
            "paddingTop": 20,
            "borderColor": "#D9D9D9",
            "borderStyle": "solid",
        },
    )
    return antd.Row(
        antd.Col(
            [
                plot,
                antd.Row(update, justify="center"),
                antd.Divider(),
                settings,
                antd.Divider(),
                inputs,
                framed_editor,
            ],
            style={"paddingRight": 20, "paddingLeft": 20},
        ),
        align="center",
        style={"paddingTop": 20},
    )
