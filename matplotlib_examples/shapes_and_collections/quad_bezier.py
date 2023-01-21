"""
============
Bezier Curve
============

This example showcases the `~.patches.PathPatch` object to create a Bezier
polycurve path patch.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/shapes_and_collections/quad_bezier.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.path as mpath
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def app():
    Path = mpath.Path
    fig, ax = plt.subplots()
    pp1 = mpatches.PathPatch(
        Path(
            [(0, 0), (1, 0), (1, 1), (0, 0)],
            [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY],
        ),
        fc="none",
        transform=ax.transData,
    )
    ax.add_patch(pp1)
    ax.plot([0.75], [0.25], "ro")
    ax.set_title("The red point should be on the path")
    return matplotlib_to_svg(fig)
