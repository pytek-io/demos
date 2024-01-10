"""
=======================
Colorbar Tick Labelling
=======================

Produce custom labelling for a colorbar.

Contributed by Scott Sinclair

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/ticks/colorbar_tick_labelling_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from numpy.random import randn

from demos.charts.utils import matplotlib_to_svg


def app(_):
    np.random.seed(19680801)
    fig, ax = plt.subplots()
    data = np.clip(randn(250, 250), -1, 1)
    cax = ax.imshow(data, cmap=cm.coolwarm)
    ax.set_title("Gaussian noise with vertical colorbar")
    cbar = fig.colorbar(cax, ticks=[-1, 0, 1])
    cbar.ax.set_yticklabels(["< -1", "0", "> 1"])
    fig, ax = plt.subplots()
    data = np.clip(randn(250, 250), -1, 1)
    cax = ax.imshow(data, cmap=cm.afmhot)
    ax.set_title("Gaussian noise with horizontal colorbar")
    cbar = fig.colorbar(cax, ticks=[-1, 0, 1], orientation="horizontal")
    cbar.ax.set_xticklabels(["Low", "Medium", "High"])
    return matplotlib_to_svg(fig)
