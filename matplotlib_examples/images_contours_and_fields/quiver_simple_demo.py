"""
==================
Quiver Simple Demo
==================

A simple example of a `~.axes.Axes.quiver` plot with a `~.axes.Axes.quiverkey`.

For more advanced options refer to
:doc:`/gallery/images_contours_and_fields/quiver_demo`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/quiver_simple_demo.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import numpy as np


def app():
    X = np.arange((-10), 10, 1)
    Y = np.arange((-10), 10, 1)
    (U, V) = np.meshgrid(X, Y)
    (fig, ax) = plt.subplots()
    q = ax.quiver(X, Y, U, V)
    ax.quiverkey(q, X=0.3, Y=1.1, U=10, label="Quiver key, length = 10", labelpos="E")
    return matplotlib_to_svg(fig)
