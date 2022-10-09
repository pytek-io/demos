"""
=============
Contourf Demo
=============

How to use the `.axes.Axes.contourf` method to create filled contour plots.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/contourf_demo.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def app():
    origin = "lower"
    delta = 0.025
    x = y = np.arange((-3.0), 3.01, delta)
    (X, Y) = np.meshgrid(x, y)
    Z1 = np.exp(((-(X**2)) - (Y**2)))
    Z2 = np.exp(((-((X - 1) ** 2)) - ((Y - 1) ** 2)))
    Z = (Z1 - Z2) * 2
    (nr, nc) = Z.shape
    Z[((-nr) // 6) :, ((-nc) // 6) :] = np.nan
    Z = np.ma.array(Z)
    Z[: (nr // 6), : (nc // 6)] = np.ma.masked
    interior = np.sqrt(((X**2) + (Y**2))) < 0.5
    Z[interior] = np.ma.masked
    (fig1, ax2) = plt.subplots(constrained_layout=True)
    CS = ax2.contourf(X, Y, Z, 10, cmap=plt.cm.bone, origin=origin)
    CS2 = ax2.contour(CS, levels=CS.levels[::2], colors="r", origin=origin)
    ax2.set_title("Nonsense (3 masked regions)")
    ax2.set_xlabel("word length anomaly")
    ax2.set_ylabel("sentence length anomaly")
    cbar = fig1.colorbar(CS)
    cbar.ax.set_ylabel("verbosity coefficient")
    cbar.add_lines(CS2)
    (fig2, ax2) = plt.subplots(constrained_layout=True)
    levels = [(-1.5), (-1), (-0.5), 0, 0.5, 1]
    CS3 = ax2.contourf(
        X, Y, Z, levels, colors=("r", "g", "b"), origin=origin, extend="both"
    )
    CS3.cmap.set_under("yellow")
    CS3.cmap.set_over("cyan")
    CS4 = ax2.contour(X, Y, Z, levels, colors=("k",), linewidths=(3,), origin=origin)
    ax2.set_title("Listed colors (3 masked regions)")
    ax2.clabel(CS4, fmt="%2.1f", colors="w", fontsize=14)
    fig2.colorbar(CS3)
    extends = ["neither", "both", "min", "max"]
    cmap = plt.colormaps["winter"].with_extremes(under="magenta", over="yellow")
    (fig, axs) = plt.subplots(2, 2, constrained_layout=True)
    for (ax, extend) in zip(axs.flat, extends):
        cs = ax.contourf(X, Y, Z, levels, cmap=cmap, extend=extend, origin=origin)
        fig.colorbar(cs, ax=ax, shrink=0.9)
        ax.set_title(("extend = %s" % extend))
        ax.locator_params(nbins=4)
    return matplotlib_to_svg(fig)
