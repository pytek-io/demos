"""
==============
Manual Contour
==============

Example of displaying your own contour lines and polygons using ContourSet.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/misc/contour_manual.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.contour import ContourSet

from demos.charts.utils import matplotlib_to_svg


def app(_):
    lines0 = [[[0, 0], [0, 4]]]
    lines1 = [[[2, 0], [1, 2], [1, 3]]]
    lines2 = [[[3, 0], [3, 2]], [[3, 3], [3, 4]]]
    filled01 = [[[0, 0], [0, 4], [1, 3], [1, 2], [2, 0]]]
    filled12 = [[[2, 0], [3, 0], [3, 2], [1, 3], [1, 2]], [[1, 4], [3, 4], [3, 3]]]
    fig, ax = plt.subplots()
    cs = ContourSet(ax, [0, 1, 2], [filled01, filled12], filled=True, cmap=cm.bone)
    cbar = fig.colorbar(cs)
    lines = ContourSet(
        ax, [0, 1, 2], [lines0, lines1, lines2], cmap=cm.cool, linewidths=3
    )
    cbar.add_lines(lines)
    ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 4.5), title="User-specified contours")
    fig, ax = plt.subplots()
    filled01 = [[[0, 0], [3, 0], [3, 3], [0, 3], [1, 1], [1, 2], [2, 2], [2, 1]]]
    kinds01 = [[1, 2, 2, 2, 1, 2, 2, 2]]
    cs = ContourSet(ax, [0, 1], [filled01], [kinds01], filled=True)
    cbar = fig.colorbar(cs)
    ax.set(
        xlim=(-0.5, 3.5),
        ylim=(-0.5, 3.5),
        title="User specified filled contours with holes",
    )
    return matplotlib_to_svg(fig)
