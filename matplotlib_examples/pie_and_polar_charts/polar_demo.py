"""
==========
Polar plot
==========

Demo of a line plot on a polar axis.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pie_and_polar_charts/polar_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    r = np.arange(0, 2, 0.01)
    theta = 2 * np.pi * r
    fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
    ax.plot(theta, r)
    ax.set_rmax(2)
    ax.set_rticks([0.5, 1, 1.5, 2])
    ax.set_rlabel_position(-22.5)
    ax.grid(True)
    ax.set_title("A line plot on a polar axis", va="bottom")
    return matplotlib_to_svg(fig)
