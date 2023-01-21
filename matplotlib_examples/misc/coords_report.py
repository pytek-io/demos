"""
=============
Coords Report
=============

Override the default reporting of coords as the mouse moves over the axes
in an interactive backend.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/misc/coords_report.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def millions(x):
    return "$%1.1fM" % (x * 1e-06)


def app():
    np.random.seed(19680801)
    x = np.random.rand(20)
    y = 10000000.0 * np.random.rand(20)
    fig, ax = plt.subplots()
    ax.fmt_ydata = millions
    plt.plot(x, y, "o")
    return matplotlib_to_svg(fig)
