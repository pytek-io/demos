"""
=====================
Demo of 3D bar charts
=====================

A basic demo of how to plot 3D bars with and without shading.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/3d_bars.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig = plt.figure(figsize=(8, 3))
    ax1 = fig.add_subplot(121, projection="3d")
    ax2 = fig.add_subplot(122, projection="3d")
    _x = np.arange(4)
    _y = np.arange(5)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    top = x + y
    bottom = np.zeros_like(top)
    width = depth = 1
    ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
    ax1.set_title("Shaded")
    ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
    ax2.set_title("Not Shaded")
    return matplotlib_to_svg(fig)
