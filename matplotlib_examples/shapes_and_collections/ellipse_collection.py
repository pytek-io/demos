"""
==================
Ellipse Collection
==================

Drawing a collection of ellipses. While this would equally be possible using
a `~.collections.EllipseCollection` or `~.collections.PathCollection`, the use
of an `~.collections.EllipseCollection` allows for much shorter code.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/shapes_and_collections/ellipse_collection.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import EllipseCollection


def app():
    x = np.arange(10)
    y = np.arange(15)
    (X, Y) = np.meshgrid(x, y)
    XY = np.column_stack((X.ravel(), Y.ravel()))
    ww = X / 10.0
    hh = Y / 15.0
    aa = X * 9
    (fig, ax) = plt.subplots()
    ec = EllipseCollection(
        ww, hh, aa, units="x", offsets=XY, offset_transform=ax.transData
    )
    ec.set_array((X + Y).ravel())
    ax.add_collection(ec)
    ax.autoscale_view()
    ax.set_xlabel("X")
    ax.set_ylabel("y")
    cbar = plt.colorbar(ec)
    cbar.set_label("X+Y")
    return matplotlib_to_svg(fig)
