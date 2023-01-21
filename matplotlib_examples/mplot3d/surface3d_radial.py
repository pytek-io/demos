"""
=================================
3D surface with polar coordinates
=================================

Demonstrates plotting a surface defined in polar coordinates.
Uses the reversed version of the YlGnBu colormap.
Also demonstrates writing axis labels with latex math mode.

Example contributed by Armin Moser.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/surface3d_radial.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    r = np.linspace(0, 1.25, 50)
    p = np.linspace(0, 2 * np.pi, 50)
    R, P = np.meshgrid(r, p)
    Z = (R**2 - 1) ** 2
    X, Y = R * np.cos(P), R * np.sin(P)
    ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
    ax.set_zlim(0, 1)
    ax.set_xlabel("$\\phi_\\mathrm{real}$")
    ax.set_ylabel("$\\phi_\\mathrm{im}$")
    ax.set_zlabel("$V(\\phi)$")
    return matplotlib_to_svg(fig)
