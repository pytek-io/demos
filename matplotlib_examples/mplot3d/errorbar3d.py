"""
============
3D errorbars
============

An example of using errorbars with upper and lower limits in mplot3d.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/errorbar3d.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    t = np.arange(0, 2 * np.pi + 0.1, 0.01)
    x, y, z = np.sin(t), np.cos(3 * t), np.sin(5 * t)
    estep = 15
    i = np.arange(t.size)
    zuplims = (i % estep == 0) & (i // estep % 3 == 0)
    zlolims = (i % estep == 0) & (i // estep % 3 == 2)
    ax.errorbar(x, y, z, 0.2, zuplims=zuplims, zlolims=zlolims, errorevery=estep)
    ax.set_xlabel("X label")
    ax.set_ylabel("Y label")
    ax.set_zlabel("Z label")
    return matplotlib_to_svg(fig)
