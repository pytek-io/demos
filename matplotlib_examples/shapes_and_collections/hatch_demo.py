"""
==========
Hatch demo
==========

Hatches can be added to most polygons in Matplotlib, including `~.Axes.bar`,
`~.Axes.fill_between`, `~.Axes.contourf`, and children of `~.patches.Polygon`.
They are currently supported in the PS, PDF, SVG, OSX, and Agg backends. The WX
and Cairo backends do not currently support hatching.

See also :doc:`/gallery/images_contours_and_fields/contourf_hatching` for
an example using `~.Axes.contourf`, and
:doc:`/gallery/shapes_and_collections/hatch_style_reference` for swatches
of the existing hatches.


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/shapes_and_collections/hatch_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Polygon

from demos.charts.utils import matplotlib_to_svg


def app(_):
    x = np.arange(1, 5)
    y1 = np.arange(1, 5)
    y2 = np.ones(y1.shape) * 4
    fig = plt.figure()
    axs = fig.subplot_mosaic([["bar1", "patches"], ["bar2", "patches"]])
    axs["bar1"].bar(x, y1, edgecolor="black", hatch="/")
    axs["bar1"].bar(x, y2, bottom=y1, edgecolor="black", hatch="//")
    axs["bar2"].bar(x, y1, edgecolor="black", hatch=["--", "+", "x", "\\"])
    axs["bar2"].bar(x, y2, bottom=y1, edgecolor="black", hatch=["*", "o", "O", "."])
    x = np.arange(0, 40, 0.2)
    axs["patches"].fill_between(
        x, np.sin(x) * 4 + 30, y2=0, hatch="///", zorder=2, fc="c"
    )
    axs["patches"].add_patch(
        Ellipse((4, 50), 10, 10, fill=True, hatch="*", facecolor="y")
    )
    axs["patches"].add_patch(
        Polygon([(10, 20), (30, 50), (50, 10)], hatch="\\/...", facecolor="g")
    )
    axs["patches"].set_xlim([0, 40])
    axs["patches"].set_ylim([10, 60])
    axs["patches"].set_aspect(1)
    return matplotlib_to_svg(fig)
