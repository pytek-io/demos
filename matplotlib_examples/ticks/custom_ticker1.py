"""
=============
Custom Ticker
=============

The :mod:`matplotlib.ticker` module defines many preset tickers, but was
primarily designed for extensibility, i.e., to support user customized ticking.

In this example, a user defined function is used to format the ticks in
millions of dollars on the y axis.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/ticks/custom_ticker1.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def millions(x, pos):
    """The two arguments are the value and tick position."""
    return "${:1.1f}M".format(x * 1e-06)


def app():
    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(millions)
    money = [150000.0, 2500000.0, 5500000.0, 20000000.0]
    ax.bar(["Bill", "Fred", "Mary", "Sue"], money)
    return matplotlib_to_svg(fig)
