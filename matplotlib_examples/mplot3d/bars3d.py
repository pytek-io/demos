"""
========================================
Create 2D bar graphs in different planes
========================================

Demonstrates making a 3D plot which has 2D bar graphs projected onto
planes y=0, y=1, etc.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/bars3d.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    np.random.seed(19680801)
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    colors = ["r", "g", "b", "y"]
    yticks = [3, 2, 1, 0]
    for c, k in zip(colors, yticks):
        xs = np.arange(20)
        ys = np.random.rand(20)
        cs = [c] * len(xs)
        cs[0] = "c"
        ax.bar(xs, ys, zs=k, zdir="y", color=cs, alpha=0.8)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_yticks(yticks)
    return matplotlib_to_svg(fig)
