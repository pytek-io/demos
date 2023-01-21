"""
==============
Triinterp Demo
==============

Interpolation from triangular grid to quad grid.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/triinterp_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    x = np.asarray([0, 1, 2, 3, 0.5, 1.5, 2.5, 1, 2, 1.5])
    y = np.asarray([0, 0, 0, 0, 1.0, 1.0, 1.0, 2, 2, 3.0])
    triangles = [
        [0, 1, 4],
        [1, 2, 5],
        [2, 3, 6],
        [1, 5, 4],
        [2, 6, 5],
        [4, 5, 7],
        [5, 6, 8],
        [5, 8, 7],
        [7, 8, 9],
    ]
    triang = mtri.Triangulation(x, y, triangles)
    z = np.cos(1.5 * x) * np.cos(1.5 * y)
    xi, yi = np.meshgrid(np.linspace(0, 3, 20), np.linspace(0, 3, 20))
    interp_lin = mtri.LinearTriInterpolator(triang, z)
    zi_lin = interp_lin(xi, yi)
    interp_cubic_geom = mtri.CubicTriInterpolator(triang, z, kind="geom")
    zi_cubic_geom = interp_cubic_geom(xi, yi)
    interp_cubic_min_E = mtri.CubicTriInterpolator(triang, z, kind="min_E")
    zi_cubic_min_E = interp_cubic_min_E(xi, yi)
    fig, axs = plt.subplots(nrows=2, ncols=2)
    axs = axs.flatten()
    axs[0].tricontourf(triang, z)
    axs[0].triplot(triang, "ko-")
    axs[0].set_title("Triangular grid")
    axs[1].contourf(xi, yi, zi_lin)
    axs[1].plot(xi, yi, "k-", lw=0.5, alpha=0.5)
    axs[1].plot(xi.T, yi.T, "k-", lw=0.5, alpha=0.5)
    axs[1].set_title("Linear interpolation")
    axs[2].contourf(xi, yi, zi_cubic_geom)
    axs[2].plot(xi, yi, "k-", lw=0.5, alpha=0.5)
    axs[2].plot(xi.T, yi.T, "k-", lw=0.5, alpha=0.5)
    axs[2].set_title("Cubic interpolation,\nkind='geom'")
    axs[3].contourf(xi, yi, zi_cubic_min_E)
    axs[3].plot(xi, yi, "k-", lw=0.5, alpha=0.5)
    axs[3].plot(xi.T, yi.T, "k-", lw=0.5, alpha=0.5)
    axs[3].set_title("Cubic interpolation,\nkind='min_E'")
    fig.tight_layout()
    return matplotlib_to_svg(fig)
