"""
================================
Reference for Matplotlib artists
================================

This example displays several of Matplotlib's graphics primitives (artists)
drawn using matplotlib API. A full list of artists and the documentation is
available at :ref:`the artist API <artist-api>`.

Copyright (c) 2010, Bartosz Telenczuk
BSD License

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/shapes_and_collections/artist_reference.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PatchCollection

from demos.charts.utils import matplotlib_to_svg


def label(xy, text):
    y = xy[1] - 0.15
    plt.text(xy[0], y, text, ha="center", family="sans-serif", size=14)


def app(_):
    fig, ax = plt.subplots()
    grid = np.mgrid[0.2:0.8:3.0j, 0.2:0.8:3.0j].reshape(2, -1).T
    patches = []
    circle = mpatches.Circle(grid[0], 0.1, ec="none")
    patches.append(circle)
    label(grid[0], "Circle")
    rect = mpatches.Rectangle(grid[1] - [0.025, 0.05], 0.05, 0.1, ec="none")
    patches.append(rect)
    label(grid[1], "Rectangle")
    wedge = mpatches.Wedge(grid[2], 0.1, 30, 270, ec="none")
    patches.append(wedge)
    label(grid[2], "Wedge")
    polygon = mpatches.RegularPolygon(grid[3], 5, 0.1)
    patches.append(polygon)
    label(grid[3], "Polygon")
    ellipse = mpatches.Ellipse(grid[4], 0.2, 0.1)
    patches.append(ellipse)
    label(grid[4], "Ellipse")
    arrow = mpatches.Arrow(grid[5, 0] - 0.05, grid[5, 1] - 0.05, 0.1, 0.1, width=0.1)
    patches.append(arrow)
    label(grid[5], "Arrow")
    Path = mpath.Path
    path_data = [
        (Path.MOVETO, [0.018, -0.11]),
        (Path.CURVE4, [-0.031, -0.051]),
        (Path.CURVE4, [-0.115, 0.073]),
        (Path.CURVE4, [-0.03, 0.073]),
        (Path.LINETO, [-0.011, 0.039]),
        (Path.CURVE4, [0.043, 0.121]),
        (Path.CURVE4, [0.075, -0.005]),
        (Path.CURVE4, [0.035, -0.027]),
        (Path.CLOSEPOLY, [0.018, -0.11]),
    ]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts + grid[6], codes)
    patch = mpatches.PathPatch(path)
    patches.append(patch)
    label(grid[6], "PathPatch")
    fancybox = mpatches.FancyBboxPatch(
        grid[7] - [0.025, 0.05],
        0.05,
        0.1,
        boxstyle=mpatches.BoxStyle("Round", pad=0.02),
    )
    patches.append(fancybox)
    label(grid[7], "FancyBboxPatch")
    x, y = [-0.06, 0.0, 0.1], [0.05, -0.05, 0.05]
    line = mlines.Line2D(x + grid[8, 0], y + grid[8, 1], lw=5.0, alpha=0.3)
    label(grid[8], "Line2D")
    colors = np.linspace(0, 1, len(patches))
    collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3)
    collection.set_array(colors)
    ax.add_collection(collection)
    ax.add_line(line)
    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    return matplotlib_to_svg(fig)
