"""
====================================
Automatically setting tick positions
====================================

Setting the behavior of tick auto-placement.

By default, Matplotlib will choose the number of ticks and tick positions so
that there is a reasonable number of ticks on the axis and they are located
at "round" numbers.

As a result, there may be no ticks on the edges of the plot.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/ticks/auto_ticks.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import numpy as np


def app():
    np.random.seed(19680801)
    (fig, ax) = plt.subplots()
    dots = np.linspace(0.3, 1.2, 10)
    (X, Y) = np.meshgrid(dots, dots)
    (x, y) = (X.ravel(), Y.ravel())
    ax.scatter(x, y, c=(x + y))
    plt.rcParams["axes.autolimit_mode"] = "round_numbers"
    (fig, ax) = plt.subplots()
    ax.scatter(x, y, c=(x + y))
    (fig, ax) = plt.subplots()
    ax.scatter(x, y, c=(x + y))
    ax.set_xmargin(0.8)
    return matplotlib_to_svg(fig)
