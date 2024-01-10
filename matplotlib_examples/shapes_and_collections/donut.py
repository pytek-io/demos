"""
=============
Mmh Donuts!!!
=============

Draw donuts (miam!) using `~.path.Path`\\s and `~.patches.PathPatch`\\es.
This example shows the effect of the path's orientations in a compound path.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/shapes_and_collections/donut.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def wise(v):
    if v == 1:
        return "CCW"
    else:
        return "CW"


def make_circle(r):
    t = np.arange(0, np.pi * 2.0, 0.01)
    t = t.reshape((len(t), 1))
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.hstack((x, y))


def app(_):
    Path = mpath.Path
    fig, ax = plt.subplots()
    inside_vertices = make_circle(0.5)
    outside_vertices = make_circle(1.0)
    codes = (
        np.ones(len(inside_vertices), dtype=mpath.Path.code_type) * mpath.Path.LINETO
    )
    codes[0] = mpath.Path.MOVETO
    for i, (inside, outside) in enumerate(((1, 1), (1, -1), (-1, 1), (-1, -1))):
        vertices = np.concatenate(
            (outside_vertices[::outside], inside_vertices[::inside])
        )
        vertices[:, (0)] += i * 2.5
        all_codes = np.concatenate((codes, codes))
        path = mpath.Path(vertices, all_codes)
        patch = mpatches.PathPatch(path, facecolor="#885500", edgecolor="black")
        ax.add_patch(patch)
        ax.annotate(
            "Outside %s,\nInside %s" % (wise(outside), wise(inside)),
            (i * 2.5, -1.5),
            va="top",
            ha="center",
        )
    ax.set_xlim(-2, 10)
    ax.set_ylim(-3, 2)
    ax.set_title("Mmm, donuts!")
    ax.set_aspect(1.0)
    return matplotlib_to_svg(fig)
