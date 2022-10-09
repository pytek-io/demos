"""
=====================================================
The histogram (hist) function with multiple data sets
=====================================================

Plot histogram with multiple sample sets and demonstrate:

* Use of legend with multiple sample sets
* Stacked bars
* Step curve with no fill
* Data sets of different sample sizes

Selecting different bin counts and sizes can significantly affect the
shape of a histogram. The Astropy docs have a great section on how to
select these parameters:
http://docs.astropy.org/en/stable/visualization/histogram.html

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/statistics/histogram_multihist.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def app():
    np.random.seed(19680801)
    n_bins = 10
    x = np.random.randn(1000, 3)
    (fig, ((ax0, ax1), (ax2, ax3))) = plt.subplots(nrows=2, ncols=2)
    colors = ["red", "tan", "lime"]
    ax0.hist(x, n_bins, density=True, histtype="bar", color=colors, label=colors)
    ax0.legend(prop={"size": 10})
    ax0.set_title("bars with legend")
    ax1.hist(x, n_bins, density=True, histtype="bar", stacked=True)
    ax1.set_title("stacked bar")
    ax2.hist(x, n_bins, histtype="step", stacked=True, fill=False)
    ax2.set_title("stack step (unfilled)")
    x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]
    ax3.hist(x_multi, n_bins, histtype="bar")
    ax3.set_title("different sample sizes")
    fig.tight_layout()
    return matplotlib_to_svg(fig)
