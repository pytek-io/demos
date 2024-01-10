"""
=================
Contourf Hatching
=================

Demo filled contour plots with hatched patterns.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/contourf_hatching.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    x = np.linspace(-3, 5, 150).reshape(1, -1)
    y = np.linspace(-3, 5, 120).reshape(-1, 1)
    z = np.cos(x) + np.sin(y)
    x, y = x.flatten(), y.flatten()
    fig, ax1 = plt.subplots()
    cs = ax1.contourf(
        x, y, z, hatches=["-", "/", "\\", "//"], cmap="gray", extend="both", alpha=0.5
    )
    fig.colorbar(cs)
    fig, ax2 = plt.subplots()
    n_levels = 6
    ax2.contour(x, y, z, n_levels, colors="black", linestyles="-")
    cs = ax2.contourf(
        x,
        y,
        z,
        n_levels,
        colors="none",
        hatches=[".", "/", "\\", None, "\\\\", "*"],
        extend="lower",
    )
    artists, labels = cs.legend_elements(str_format="{:2.1f}".format)
    ax2.legend(artists, labels, handleheight=2, framealpha=1)
    return matplotlib_to_svg(fig)
