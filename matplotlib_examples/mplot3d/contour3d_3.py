"""
========================================
Projecting contour profiles onto a graph
========================================

Demonstrates displaying a 3D surface while also projecting contour 'profiles'
onto the 'walls' of the graph.

See contourf3d_demo2 for the filled version.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/contour3d_3.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm


def app():
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    (X, Y, Z) = axes3d.get_test_data(0.05)
    ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
    ax.contour(X, Y, Z, zdir="z", offset=(-100), cmap=cm.coolwarm)
    ax.contour(X, Y, Z, zdir="x", offset=(-40), cmap=cm.coolwarm)
    ax.contour(X, Y, Z, zdir="y", offset=40, cmap=cm.coolwarm)
    ax.set(
        xlim=((-40), 40),
        ylim=((-40), 40),
        zlim=((-100), 100),
        xlabel="X",
        ylabel="Y",
        zlabel="Z",
    )
    return matplotlib_to_svg(fig)
