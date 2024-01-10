"""
==================================
Scatter Histogram (Locatable Axes)
==================================

Show the marginal distributions of a scatter plot as histograms at the sides of
the plot.

For a nice alignment of the main axes with the marginals, the axes positions
are defined by a ``Divider``, produced via `.make_axes_locatable`.  Note that
the ``Divider`` API allows setting axes sizes and pads in inches, which is its
main feature.

If one wants to set axes sizes and pads relative to the main Figure, see the
:doc:`/gallery/lines_bars_and_markers/scatter_hist` example.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/scatter_hist_locatable_axes.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

from demos.charts.utils import matplotlib_to_svg


def app(_):
    np.random.seed(19680801)
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    ax.scatter(x, y)
    ax.set_aspect(1.0)
    divider = make_axes_locatable(ax)
    ax_histx = divider.append_axes("top", 1.2, pad=0.1, sharex=ax)
    ax_histy = divider.append_axes("right", 1.2, pad=0.1, sharey=ax)
    ax_histx.xaxis.set_tick_params(labelbottom=False)
    ax_histy.yaxis.set_tick_params(labelleft=False)
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax / binwidth) + 1) * binwidth
    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation="horizontal")
    ax_histx.set_yticks([0, 50, 100])
    ax_histy.set_xticks([0, 50, 100])
    return matplotlib_to_svg(fig)
