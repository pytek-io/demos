"""
================
Parametric Curve
================

This example demonstrates plotting a parametric curve in 3D.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/lines3d.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def app():
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    theta = np.linspace(((-4) * np.pi), (4 * np.pi), 100)
    z = np.linspace((-2), 2, 100)
    r = (z**2) + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    ax.plot(x, y, z, label="parametric curve")
    ax.legend()
    return matplotlib_to_svg(fig)
