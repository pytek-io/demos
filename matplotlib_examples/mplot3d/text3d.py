"""
======================
Text annotations in 3D
======================

Demonstrates the placement of text annotations on a 3D plot.

Functionality shown:

- Using the text function with three types of 'zdir' values: None, an axis
  name (ex. 'x'), or a direction tuple (ex. (1, 1, 0)).
- Using the text function with the color keyword.
- Using the text2D function to place text on a fixed position on the ax
  object.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/text3d.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt


def app():
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    zdirs = (None, "x", "y", "z", (1, 1, 0), (1, 1, 1))
    xs = (1, 4, 4, 9, 4, 1)
    ys = (2, 5, 8, 10, 1, 2)
    zs = (10, 3, 8, 9, 1, 8)
    for (zdir, x, y, z) in zip(zdirs, xs, ys, zs):
        label = "(%d, %d, %d), dir=%s" % (x, y, z, zdir)
        ax.text(x, y, z, label, zdir)
    ax.text(9, 0, 0, "red", color="red")
    ax.text2D(0.05, 0.95, "2D Text", transform=ax.transAxes)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    return matplotlib_to_svg(fig)
