"""
=======
3D stem
=======

Demonstration of a stem plot in 3D, which plots vertical lines from a baseline
to the *z*-coordinate and places a marker at the tip.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/stem3d_demo.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import numpy as np


def app():
    theta = np.linspace(0, (2 * np.pi))
    x = np.cos((theta - (np.pi / 2)))
    y = np.sin((theta - (np.pi / 2)))
    z = theta
    (fig, ax) = plt.subplots(subplot_kw=dict(projection="3d"))
    ax.stem(x, y, z)
    (fig, ax) = plt.subplots(subplot_kw=dict(projection="3d"))
    (markerline, stemlines, baseline) = ax.stem(
        x, y, z, linefmt="grey", markerfmt="D", bottom=np.pi
    )
    markerline.set_markerfacecolor("none")
    (fig, ax) = plt.subplots(subplot_kw=dict(projection="3d"))
    (markerline, stemlines, baseline) = ax.stem(x, y, z, bottom=(-1), orientation="x")
    ax.set(xlabel="x", ylabel="y", zlabel="z")
    return matplotlib_to_svg(fig)
