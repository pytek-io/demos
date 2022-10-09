"""
==========================
Scatter plot on polar axis
==========================

Size increases radially in this example and color increases with angle
(just to verify the symbols are being scattered correctly).

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pie_and_polar_charts/polar_scatter.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def app():
    np.random.seed(19680801)
    N = 150
    r = 2 * np.random.rand(N)
    theta = (2 * np.pi) * np.random.rand(N)
    area = 200 * (r**2)
    colors = theta
    fig = plt.figure()
    ax = fig.add_subplot(projection="polar")
    c = ax.scatter(theta, r, c=colors, s=area, cmap="hsv", alpha=0.75)
    fig = plt.figure()
    ax = fig.add_subplot(projection="polar")
    c = ax.scatter(theta, r, c=colors, s=area, cmap="hsv", alpha=0.75)
    ax.set_rorigin((-2.5))
    ax.set_theta_zero_location("W", offset=10)
    fig = plt.figure()
    ax = fig.add_subplot(projection="polar")
    c = ax.scatter(theta, r, c=colors, s=area, cmap="hsv", alpha=0.75)
    ax.set_thetamin(45)
    ax.set_thetamax(135)
    return matplotlib_to_svg(fig)
