"""
=============================================
Generate polygons to fill under 3D line graph
=============================================

Demonstrate how to create polygons which fill the space under a line
graph. In this example polygons are semi-transparent, creating a sort
of 'jagged stained glass' effect.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/polys3d.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import math
import numpy as np

np.random.seed(19680801)


def polygon_under_graph(x, y):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (x, y) line graph. This assumes x is in ascending order.
    """
    return [(x[0], 0.0), *zip(x, y), (x[(-1)], 0.0)]


def app():
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    x = np.linspace(0.0, 10.0, 31)
    lambdas = range(1, 9)
    gamma = np.vectorize(math.gamma)
    verts = [
        polygon_under_graph(x, (((l**x) * np.exp((-l))) / gamma((x + 1))))
        for l in lambdas
    ]
    facecolors = plt.colormaps["viridis_r"](np.linspace(0, 1, len(verts)))
    poly = PolyCollection(verts, facecolors=facecolors, alpha=0.7)
    ax.add_collection3d(poly, zs=lambdas, zdir="y")
    ax.set(
        xlim=(0, 10),
        ylim=(1, 9),
        zlim=(0, 0.35),
        xlabel="x",
        ylabel="$\\lambda$",
        zlabel="probability",
    )
    return matplotlib_to_svg(fig)
