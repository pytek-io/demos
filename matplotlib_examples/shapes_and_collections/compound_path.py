"""
=============
Compound path
=============

Make a compound path -- in this case two simple polygons, a rectangle
and a triangle.  Use ``CLOSEPOLY`` and ``MOVETO`` for the different parts of
the compound path

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/shapes_and_collections/compound_path.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt


def app():
    vertices = []
    codes = []
    codes = ([Path.MOVETO] + ([Path.LINETO] * 3)) + [Path.CLOSEPOLY]
    vertices = [(1, 1), (1, 2), (2, 2), (2, 1), (0, 0)]
    codes += ([Path.MOVETO] + ([Path.LINETO] * 2)) + [Path.CLOSEPOLY]
    vertices += [(4, 4), (5, 5), (5, 4), (0, 0)]
    path = Path(vertices, codes)
    pathpatch = PathPatch(path, facecolor="none", edgecolor="green")
    (fig, ax) = plt.subplots()
    ax.add_patch(pathpatch)
    ax.set_title("A compound path")
    ax.autoscale_view()
    return matplotlib_to_svg(fig)
