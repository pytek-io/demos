"""
=================
Errorbar function
=================

This exhibits the most basic use of the error bar method.
In this case, constant values are provided for the error
in both the x- and y-directions.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/statistics/errorbar.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def app():
    x = np.arange(0.1, 4, 0.5)
    y = np.exp((-x))
    (fig, ax) = plt.subplots()
    ax.errorbar(x, y, xerr=0.2, yerr=0.4)
    return matplotlib_to_svg(fig)