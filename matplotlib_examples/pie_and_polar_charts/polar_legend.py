"""
============
Polar Legend
============

Demo of a legend on a polar-axis plot.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pie_and_polar_charts/polar_legend.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    fig = plt.figure()
    ax = fig.add_subplot(projection="polar", facecolor="lightgoldenrodyellow")
    r = np.linspace(0, 3, 301)
    theta = 2 * np.pi * r
    ax.plot(theta, r, color="tab:orange", lw=3, label="a line")
    ax.plot(0.5 * theta, r, color="tab:blue", ls="--", lw=3, label="another line")
    ax.tick_params(grid_color="palegoldenrod")
    angle = np.deg2rad(67.5)
    ax.legend(
        loc="lower left",
        bbox_to_anchor=(0.5 + np.cos(angle) / 2, 0.5 + np.sin(angle) / 2),
    )
    return matplotlib_to_svg(fig)
