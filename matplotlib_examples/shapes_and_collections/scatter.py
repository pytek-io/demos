"""
============
Scatter plot
============

This example showcases a simple scatter plot.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/shapes_and_collections/scatter.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def app():
    np.random.seed(19680801)
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N)) ** 2
    fig = plt.figure()
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    return matplotlib_to_svg(fig)