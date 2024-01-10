"""
=======================
Adding lines to figures
=======================

Adding lines to a figure without any axes.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/fig_x.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.lines as lines
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig = plt.figure()
    fig.add_artist(lines.Line2D([0, 1], [0, 1]))
    fig.add_artist(lines.Line2D([0, 1], [1, 0]))
    return matplotlib_to_svg(fig)
