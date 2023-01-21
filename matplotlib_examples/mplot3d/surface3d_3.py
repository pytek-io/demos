"""
=========================
3D surface (checkerboard)
=========================

Demonstrates plotting a 3D surface colored in a checkerboard pattern.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/surface3d_3.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator

from demos.charts.utils import matplotlib_to_svg


def app():
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    X = np.arange(-5, 5, 0.25)
    xlen = len(X)
    Y = np.arange(-5, 5, 0.25)
    ylen = len(Y)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    colortuple = "y", "b"
    colors = np.empty(X.shape, dtype=str)
    for y in range(ylen):
        for x in range(xlen):
            colors[y, x] = colortuple[(x + y) % len(colortuple)]
    surf = ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0)
    ax.set_zlim(-1, 1)
    ax.zaxis.set_major_locator(LinearLocator(6))
    return matplotlib_to_svg(fig)
