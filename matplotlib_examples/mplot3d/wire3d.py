"""
=================
3D wireframe plot
=================

A very basic demonstration of a wireframe plot.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/wire3d.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


def app():
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    (X, Y, Z) = axes3d.get_test_data(0.05)
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    return matplotlib_to_svg(fig)
