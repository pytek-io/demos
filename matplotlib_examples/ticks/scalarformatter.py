"""
==========================
The default tick formatter
==========================

The example shows use of the default `.ScalarFormatter` with different
settings.

Example 1 : Default

Example 2 : With no Numerical Offset

Example 3 : With Mathtext

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/ticks/scalarformatter.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import numpy as np


def app():
    x = np.arange(0, 1, 0.01)
    (fig, [[ax1, ax2], [ax3, ax4]]) = plt.subplots(2, 2, figsize=(6, 6))
    fig.text(
        0.5,
        0.975,
        "Default settings",
        horizontalalignment="center",
        verticalalignment="top",
    )
    ax1.plot(((x * 100000.0) + 10000000000.0), ((x * 1e-10) + 1e-05))
    ax2.plot((x * 100000.0), (x * 0.0001))
    ax3.plot((((-x) * 100000.0) - 10000000000.0), (((-x) * 1e-05) - 1e-10))
    ax4.plot(((-x) * 100000.0), ((-x) * 0.0001))
    fig.subplots_adjust(wspace=0.7, hspace=0.6)
    x = np.arange(0, 1, 0.01)
    (fig, [[ax1, ax2], [ax3, ax4]]) = plt.subplots(2, 2, figsize=(6, 6))
    fig.text(
        0.5,
        0.975,
        "No numerical offset",
        horizontalalignment="center",
        verticalalignment="top",
    )
    ax1.plot(((x * 100000.0) + 10000000000.0), ((x * 1e-10) + 1e-05))
    ax1.ticklabel_format(useOffset=False)
    ax2.plot((x * 100000.0), (x * 0.0001))
    ax2.ticklabel_format(useOffset=False)
    ax3.plot((((-x) * 100000.0) - 10000000000.0), (((-x) * 1e-05) - 1e-10))
    ax3.ticklabel_format(useOffset=False)
    ax4.plot(((-x) * 100000.0), ((-x) * 0.0001))
    ax4.ticklabel_format(useOffset=False)
    fig.subplots_adjust(wspace=0.7, hspace=0.6)
    x = np.arange(0, 1, 0.01)
    (fig, [[ax1, ax2], [ax3, ax4]]) = plt.subplots(2, 2, figsize=(6, 6))
    fig.text(
        0.5,
        0.975,
        "With mathtext",
        horizontalalignment="center",
        verticalalignment="top",
    )
    ax1.plot(((x * 100000.0) + 10000000000.0), ((x * 1e-10) + 1e-05))
    ax1.ticklabel_format(useMathText=True)
    ax2.plot((x * 100000.0), (x * 0.0001))
    ax2.ticklabel_format(useMathText=True)
    ax3.plot((((-x) * 100000.0) - 10000000000.0), (((-x) * 1e-05) - 1e-10))
    ax3.ticklabel_format(useMathText=True)
    ax4.plot(((-x) * 100000.0), ((-x) * 0.0001))
    ax4.ticklabel_format(useMathText=True)
    fig.subplots_adjust(wspace=0.7, hspace=0.6)
    return matplotlib_to_svg(fig)
