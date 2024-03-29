"""
=======================================
Advanced quiver and quiverkey functions
=======================================

Demonstrates some more advanced options for `~.axes.Axes.quiver`.  For a simple
example refer to :doc:`/gallery/images_contours_and_fields/quiver_simple_demo`.

Note: The plot autoscaling does not take into account the arrows, so
those on the boundaries may reach out of the picture.  This is not an easy
problem to solve in a perfectly general way.  The recommended workaround is to
manually set the Axes limits in such a case.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/quiver_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    X, Y = np.meshgrid(np.arange(0, 2 * np.pi, 0.2), np.arange(0, 2 * np.pi, 0.2))
    U = np.cos(X)
    V = np.sin(Y)
    fig1, ax1 = plt.subplots()
    ax1.set_title("Arrows scale with plot width, not view")
    Q = ax1.quiver(X, Y, U, V, units="width")
    qk = ax1.quiverkey(
        Q, 0.9, 0.9, 2, "$2 \\frac{m}{s}$", labelpos="E", coordinates="figure"
    )
    fig2, ax2 = plt.subplots()
    ax2.set_title("pivot='mid'; every third arrow; units='inches'")
    Q = ax2.quiver(
        X[::3, ::3], Y[::3, ::3], U[::3, ::3], V[::3, ::3], pivot="mid", units="inches"
    )
    qk = ax2.quiverkey(
        Q, 0.9, 0.9, 1, "$1 \\frac{m}{s}$", labelpos="E", coordinates="figure"
    )
    ax2.scatter(X[::3, ::3], Y[::3, ::3], color="r", s=5)
    fig, ax3 = plt.subplots()
    ax3.set_title("pivot='tip'; scales with x view")
    M = np.hypot(U, V)
    Q = ax3.quiver(X, Y, U, V, M, units="x", pivot="tip", width=0.022, scale=1 / 0.15)
    qk = ax3.quiverkey(
        Q, 0.9, 0.9, 1, "$1 \\frac{m}{s}$", labelpos="E", coordinates="figure"
    )
    ax3.scatter(X, Y, color="0.5", s=1)
    return matplotlib_to_svg(fig)
