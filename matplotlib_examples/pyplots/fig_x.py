"""
=======================
Adding lines to figures
=======================

Adding lines to a figure without any axes.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/fig_x.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import matplotlib.lines as lines


def app():
    fig = plt.figure()
    fig.add_artist(lines.Line2D([0, 1], [0, 1]))
    fig.add_artist(lines.Line2D([0, 1], [1, 0]))
    return matplotlib_to_svg(fig)
