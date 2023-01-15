"""Fetch historical data from yahoo in real time, plot time series and signals using plotly."""
import datetime
import io
import itertools
import json
import pathlib
from dataclasses import dataclass

import httpx
import pandas as pd
import plotly.graph_objects as go
import reflect as r
import reflect_antd as antd
import reflect_html as html
import reflect_monaco as monaco
import reflect_plotly as plotly
from plotly.subplots import make_subplots

from ..fred import get_fred_series_observations

YAHOO_URL = "https://query1.finance.yahoo.com/v7/finance/download/"
TICKERS_PATH = "stock_prices/nasdaq/nasdaq.json"

filter_options = r.JSMethod(
    "filter",
    "return option.value.toUpperCase().indexOf(inputValue.toUpperCase()) !== -1",
    "inputValue",
    "option",
)

tickers = {
    record["symbol"]: record["name"]
    for record in json.loads(
        pathlib.Path(__file__).parent.parent.joinpath(TICKERS_PATH).read_text()
    )["data"]["table"]["rows"]
}


def create_timeseries_settings_layout(*elements):
    return antd.Row(
        [
            antd.Col(element, span=span)
            for element, span in zip(elements, [5, 4, 2, 8, 5])
        ],
        align="middle",
        style={"height": "100%", "marginTop": 10},
        gutter={"xs": 8, "sm": 16, "md": 24, "lg": 32},
    )


def merge_dict(d1, d2):
    result = d1
    for k, v in d2.items():
        if (
            k in result
            and isinstance(result[k], dict)
            and isinstance(v, dict)
        ):
            merge_dict(result[k], v)
        else:
            result[k] = v
    return result


def input_panel(signal_definitions_obs):
    signal_count = itertools.count(1)
    add_signal = lambda: signal_definitions_obs.append(
        {"ticker": "AAPL", "name": f"stock_{next(signal_count)}", "source": "yahoo"}
    )
    add_signal()
    signal_definitions_obs.append(
        {"ticker": "T5YIE", "name": f"stock_{next(signal_count)}", "source": "fred"}
    )

    def create_timeseries_row(signal_obs_dict):
        ticker = antd.AutoComplete(
            options=[],
            # options=[{"value": ticker} for ticker in tickers],
            value=signal_obs_dict["ticker"],
            style={"textAlign": "right", "width": 100},
            filterOption=filter_options,
            allowClear=True,
        )
        return create_timeseries_settings_layout(
            antd.Input(value=signal_obs_dict["name"], style={"width": 100}),
            ticker,
            antd.Select(
                signal_obs_dict["source"],
                options=[{"value": "yahoo"}, {"value": "fred"}],
            ),
            antd.Typography(
                lambda: tickers.get(ticker()),
                style={
                    "width": 400,
                    "height": 30,
                    "display": "flex",
                    "alignItems": "center",
                },
            ),
            antd.Button(
                "-",
                onClick=lambda: signal_definitions_obs.remove(signal_obs_dict),
                style={"width": 42},
            ),
        )

    signal_definitions_rows = r.Mapping(create_timeseries_row, signal_definitions_obs)
    return html.div(
        [
            create_timeseries_settings_layout(
                html.label("Name"),
                html.label("Ticker"),
                html.label("Actual name"),
                antd.Button(
                    "+",
                    onClick=add_signal,
                    style={"width": 42},
                ),
            ),
            antd.Col(signal_definitions_rows),
        ]
    )


editor_options = dict(
    minimap={"enabled": False},
    lineNumbers=False,
    glyphMargin=False,
    wordWrap=True,
    renderValidationDecorations="off" if False else "on",
)


def get_yahoo_data(ticker, start, end):
    url = f"{YAHOO_URL}{ticker}?period1={int(start.timestamp())}&period2={int(end.timestamp())}&interval=1d&events=history"
    try:
        return pd.read_csv(io.BytesIO(httpx.get(url).content))
    except Exception as exception:
        raise RuntimeError(
            f"Failed to retrieve {ticker} data from yahoo: {exception}"
        ) from exception


@dataclass
class TimeSeries:
    ticker: str
    name: str
    values: pd.DataFrame


def app(_: r.Window):
    today = datetime.datetime.today()
    signal_definitions_obs = r.ObservableList[r.DictOfObservables]()
    inputs = input_panel(signal_definitions_obs)
    editor = monaco.Editor(
        defaultValue=pathlib.Path(
            pathlib.Path(__file__).parent, "script.py"
        ).read_text(),
        height=500,
        options=editor_options,
    )
    range_slider = antd.Switch(defaultChecked=True)
    show_legends = antd.Switch(defaultChecked=True)
    start_date = antd.DatePicker(defaultValue=today - datetime.timedelta(days=365))
    end_date = antd.DatePicker(defaultValue=today)

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

    def fetch_timeseries(signal_definition):
        ticker = signal_definition["ticker"]()
        start, end = start_date(), end_date()
        if signal_definition["source"]() == "yahoo":
            data = get_yahoo_data(ticker, start, end)
        else:
            data = get_fred_series_observations(ticker, start, end)
        return signal_definition["name"](), TimeSeries(
            ticker, tickers.get(ticker), data
        )

    stock_timeseries = r.Mapping(fetch_timeseries, signal_definitions_obs)
    chart_data = r.ObservableValue({})

    async def evaluate_script():
        scripts_locals = merge_dict(locals(), stock_timeseries)
        exec(await editor.getValue(), None, scripts_locals)
        chart_data.set(scripts_locals["figure"].to_dict())

    plot = plotly.Plot(
        data=lambda: chart_data().get("data"),
        layout=lambda: merge_dict(layout(), chart_data().get("layout", {})),
        style={"height": "100%", "width": "100%"},
    )
    update = antd.Button("Update", onClick=evaluate_script)
    settings = antd.create_form_layout(
        [
            ("Start", start_date),
            ("End", end_date),
            ("Range slider", range_slider),
            ("Show legends", show_legends),
            ("Update", update),
        ]
    )
    return antd.Col(
        [
            plot,
            settings,
            inputs,
            editor,
        ],
        style={"paddingRight": 20, "paddingLeft": 20},
    )
