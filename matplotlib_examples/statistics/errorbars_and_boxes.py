"""
====================================================
Creating boxes from error bars using PatchCollection
====================================================

In this example, we snazz up a pretty standard error bar plot by adding
a rectangle patch defined by the limits of the bars in both the x- and
y- directions. To do this, we have to write our own custom function
called ``make_error_boxes``. Close inspection of this function will
reveal the preferred pattern in writing functions for matplotlib:

  1. an `~.axes.Axes` object is passed directly to the function
  2. the function operates on the ``Axes`` methods directly, not through
     the ``pyplot`` interface
  3. plotting keyword arguments that could be abbreviated are spelled out for
     better code readability in the future (for example we use *facecolor*
     instead of *fc*)
  4. the artists returned by the ``Axes`` plotting methods are then
     returned by the function so that, if desired, their styles
     can be modified later outside of the function (they are not
     modified in this example).

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/statistics/errorbars_and_boxes.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle

from demos.charts.utils import matplotlib_to_svg

n = 5
np.random.seed(19680801)
x = np.arange(0, n, 1)
y = np.random.rand(n) * 5.0
xerr = np.random.rand(2, n) + 0.1
yerr = np.random.rand(2, n) + 0.2


def make_error_boxes(
    ax, xdata, ydata, xerror, yerror, facecolor="r", edgecolor="none", alpha=0.5
):
    errorboxes = [
        Rectangle((x - xe[0], y - ye[0]), xe.sum(), ye.sum())
        for x, y, xe, ye in zip(xdata, ydata, xerror.T, yerror.T)
    ]
    pc = PatchCollection(
        errorboxes, facecolor=facecolor, alpha=alpha, edgecolor=edgecolor
    )
    ax.add_collection(pc)
    artists = ax.errorbar(
        xdata, ydata, xerr=xerror, yerr=yerror, fmt="none", ecolor="k"
    )
    return artists


def app(_):
    fig, ax = plt.subplots(1)
    _ = make_error_boxes(ax, x, y, xerr, yerr)
    return matplotlib_to_svg(fig)
