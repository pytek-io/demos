from dataclasses import dataclass

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


@dataclass
class TimeSeries:
    ticker: str
    name: str
    values: pd.DataFrame


def scatter(timeseries: pd.DataFrame, color: str):
    return go.Scatter(
        name=timeseries.ticker,
        line={"color": color},
        x=timeseries.values["date"],
        y=timeseries.values["value"],
    )


def moving_average(stock: TimeSeries, nb_days: int, color: str):
    return go.Scatter(
        name=f"MVA {stock.ticker} {nb_days} days",
        line={"color": color},
        x=stock.values["date"],
        y=stock.values["value"].rolling(nb_days).mean(),
    )


def candle_stick(yahoo_timeseries: TimeSeries):
    return go.Candlestick(
        x=yahoo_timeseries.values["Date"],
        decreasing={"line": {"color": "cyan"}},
        increasing={"line": {"color": "gray"}},
        xaxis="x",
        yaxis="y",
        name=yahoo_timeseries.ticker,
        open=yahoo_timeseries.values["Open"],
        close=yahoo_timeseries.values["Close"],
        low=yahoo_timeseries.values["Low"],
        high=yahoo_timeseries.values["High"],
    )
