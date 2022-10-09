"""
==================================================
Demonstrates plotting contour (level) curves in 3D
==================================================

This is like a contour plot in 2D except that the ``f(x, y)=c`` curve is
plotted on the plane ``z=c``.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/contour3d.py.
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
    ax.contour(X, Y, Z, cmap=cm.coolwarm)
    return matplotlib_to_svg(fig)
