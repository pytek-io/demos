"""
=======================
Bar chart on polar axis
=======================

Demo of bar plot on a polar axis.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pie_and_polar_charts/polar_bar.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig = plt.figure()
    np.random.seed(19680801)
    N = 20
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4 * np.random.rand(N)
    colors = plt.cm.viridis(radii / 10.0)
    ax = plt.subplot(projection="polar")
    ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)
    return matplotlib_to_svg(fig)
