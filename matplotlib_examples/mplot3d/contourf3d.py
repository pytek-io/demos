"""
===============
Filled contours
===============

contourf differs from contour in that it creates filled contours, ie.
a discrete number of colours are used to shade the domain.

This is like a contourf plot in 2D except that the shaded region corresponding
to the level c is graphed on the plane z=c.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/contourf3d.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    X, Y, Z = axes3d.get_test_data(0.05)
    ax.contourf(X, Y, Z, cmap=cm.coolwarm)
    return matplotlib_to_svg(fig)
