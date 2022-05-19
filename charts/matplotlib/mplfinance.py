import matplotlib

matplotlib.use("Agg")  # this is stop Python rocket from showing in Dock on Mac

import pandas as pd
from demos.charts.utils import matplotlib_to_svg

import mplfinance as mpf
import numpy as np

TITLE = "MPL Finance"


def percentB_aboveone(percentB, price):
    signal = []
    previous = 2
    for date, value in percentB.iteritems():
        if value > 1 and previous <= 1:
            signal.append(price[date] * 1.01)
        else:
            signal.append(np.nan)
        previous = value
    return signal


def percentB_belowzero(percentB, price):
    signal = []
    previous = -1.0
    for date, value in percentB.iteritems():
        if value < 0 and previous >= 0:
            signal.append(price[date] * 0.99)
        else:
            signal.append(np.nan)
        previous = value
    return signal


def app():
    file_name = "demos/charts/data/SPY_20110701_20120630_Bollinger.csv"
    df = pd.read_csv(file_name, index_col=0, parse_dates=True)
    low_signal = percentB_belowzero(df["PercentB"], df["Close"])
    high_signal = percentB_aboveone(df["PercentB"], df["Close"])
    fig, _axis_list = mpf.plot(
        df,
        returnfig=True,
        volume=True,
        addplot=[
            mpf.make_addplot(df[["LowerB", "UpperB"]]),
            mpf.make_addplot(low_signal, type="scatter", markersize=200, marker="^"),
            mpf.make_addplot(high_signal, type="scatter", markersize=200, marker="v"),
            mpf.make_addplot((df["PercentB"]), panel=1, color="g"),
        ],
    )
    return matplotlib_to_svg(fig)
