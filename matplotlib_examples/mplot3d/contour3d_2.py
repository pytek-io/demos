"""
============================================================================
Demonstrates plotting contour (level) curves in 3D using the extend3d option
============================================================================

This modification of the contour3d_demo example uses extend3d=True to
extend the curves vertically into 'ribbons'.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/contour3d_2.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

from demos.charts.utils import matplotlib_to_svg


def app():
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    X, Y, Z = axes3d.get_test_data(0.05)
    ax.contour(X, Y, Z, extend3d=True, cmap=cm.coolwarm)
    return matplotlib_to_svg(fig)
