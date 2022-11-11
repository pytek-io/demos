"""
============
Dollar Ticks
============

Use a `~.ticker.FormatStrFormatter` to prepend dollar signs on y axis labels.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/dollar_ticks.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def app():
    np.random.seed(19680801)
    (fig, ax) = plt.subplots()
    ax.plot((100 * np.random.rand(20)))
    ax.yaxis.set_major_formatter("${x:1.2f}")
    ax.yaxis.set_tick_params(
        which="major", labelcolor="green", labelleft=False, labelright=True
    )
    return matplotlib_to_svg(fig)