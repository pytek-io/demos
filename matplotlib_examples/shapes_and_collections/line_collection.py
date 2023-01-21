"""
===============
Line Collection
===============

Plotting lines with Matplotlib.

`~matplotlib.collections.LineCollection` allows one to plot multiple
lines on a figure. Below we show off some of its properties.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/shapes_and_collections/line_collection.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as mcolors
from matplotlib.collections import LineCollection

from demos.charts.utils import matplotlib_to_svg


def app():
    x = np.arange(100)
    ys = x[:50, (np.newaxis)] + x[(np.newaxis), :]
    segs = np.zeros((50, 100, 2))
    segs[:, :, (1)] = ys
    segs[:, :, (0)] = x
    segs = np.ma.masked_where((segs > 50) & (segs < 60), segs)
    fig, ax = plt.subplots()
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(ys.min(), ys.max())
    colors = [
        mcolors.to_rgba(c) for c in plt.rcParams["axes.prop_cycle"].by_key()["color"]
    ]
    line_segments = LineCollection(
        segs, linewidths=(0.5, 1, 1.5, 2), colors=colors, linestyle="solid"
    )
    ax.add_collection(line_segments)
    ax.set_title("Line collection with masked arrays")
    N = 50
    x = np.arange(N)
    ys = [(x + i) for i in x]
    fig, ax = plt.subplots()
    ax.set_xlim(np.min(x), np.max(x))
    ax.set_ylim(np.min(ys), np.max(ys))
    line_segments = LineCollection(
        [np.column_stack([x, y]) for y in ys],
        linewidths=(0.5, 1, 1.5, 2),
        linestyles="solid",
    )
    line_segments.set_array(x)
    ax.add_collection(line_segments)
    axcb = fig.colorbar(line_segments)
    axcb.set_label("Line Number")
    ax.set_title("Line Collection with mapped colors")
    plt.sci(line_segments)
    return matplotlib_to_svg(fig)
