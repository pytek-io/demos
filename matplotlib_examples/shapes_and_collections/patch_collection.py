"""
============================
Circles, Wedges and Polygons
============================

This example demonstrates how to use `.collections.PatchCollection`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/shapes_and_collections/patch_collection.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle, Polygon, Wedge

from demos.charts.utils import matplotlib_to_svg


def app():
    np.random.seed(19680801)
    fig, ax = plt.subplots()
    resolution = 50
    N = 3
    x = np.random.rand(N)
    y = np.random.rand(N)
    radii = 0.1 * np.random.rand(N)
    patches = []
    for x1, y1, r in zip(x, y, radii):
        circle = Circle((x1, y1), r)
        patches.append(circle)
    x = np.random.rand(N)
    y = np.random.rand(N)
    radii = 0.1 * np.random.rand(N)
    theta1 = 360.0 * np.random.rand(N)
    theta2 = 360.0 * np.random.rand(N)
    for x1, y1, r, t1, t2 in zip(x, y, radii, theta1, theta2):
        wedge = Wedge((x1, y1), r, t1, t2)
        patches.append(wedge)
    patches += [
        Wedge((0.3, 0.7), 0.1, 0, 360),
        Wedge((0.7, 0.8), 0.2, 0, 360, width=0.05),
        Wedge((0.8, 0.3), 0.2, 0, 45),
        Wedge((0.8, 0.3), 0.2, 45, 90, width=0.1),
    ]
    for i in range(N):
        polygon = Polygon(np.random.rand(N, 2), True)
        patches.append(polygon)
    colors = 100 * np.random.rand(len(patches))
    p = PatchCollection(patches, alpha=0.4)
    p.set_array(colors)
    ax.add_collection(p)
    fig.colorbar(p, ax=ax)
    return matplotlib_to_svg(fig)
