"""
=====================
Hexagonal binned plot
=====================

`~.Axes.hexbin` is a 2D histogram plot, in which the bins are hexagons and
the color represents the number of data points within each bin.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/statistics/hexbin_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    np.random.seed(19680801)
    n = 100000
    x = np.random.standard_normal(n)
    y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
    xlim = x.min(), x.max()
    ylim = y.min(), y.max()
    fig, (ax0, ax1) = plt.subplots(ncols=2, sharey=True, figsize=(9, 4))
    hb = ax0.hexbin(x, y, gridsize=50, cmap="inferno")
    ax0.set(xlim=xlim, ylim=ylim)
    ax0.set_title("Hexagon binning")
    cb = fig.colorbar(hb, ax=ax0, label="counts")
    hb = ax1.hexbin(x, y, gridsize=50, bins="log", cmap="inferno")
    ax1.set(xlim=xlim, ylim=ylim)
    ax1.set_title("With a log color scale")
    cb = fig.colorbar(hb, ax=ax1, label="log10(N)")
    return matplotlib_to_svg(fig)
