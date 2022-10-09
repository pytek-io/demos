"""
=========================
Fig Axes Customize Simple
=========================

Customize the background, labels and ticks of a simple plot.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/fig_axes_customize_simple.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt


def app():
    fig = plt.figure()
    rect = fig.patch
    rect.set_facecolor("lightgoldenrodyellow")
    ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
    rect = ax1.patch
    rect.set_facecolor("lightslategray")
    for label in ax1.xaxis.get_ticklabels():
        label.set_color("tab:red")
        label.set_rotation(45)
        label.set_fontsize(16)
    for line in ax1.yaxis.get_ticklines():
        line.set_color("tab:green")
        line.set_markersize(25)
        line.set_markeredgewidth(3)
    return matplotlib_to_svg(fig)
