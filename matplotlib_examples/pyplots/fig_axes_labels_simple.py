"""
==================
Simple axes labels
==================

Label the axes of a plot.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/fig_axes_labels_simple.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def app():
    fig = plt.figure()
    fig.subplots_adjust(top=0.8)
    ax1 = fig.add_subplot(211)
    ax1.set_ylabel("volts")
    ax1.set_title("a sine wave")
    t = np.arange(0.0, 1.0, 0.01)
    s = np.sin(((2 * np.pi) * t))
    (line,) = ax1.plot(t, s, lw=2)
    np.random.seed(19680801)
    ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
    (n, bins, patches) = ax2.hist(np.random.randn(1000), 50)
    ax2.set_xlabel("time (s)")
    return matplotlib_to_svg(fig)
