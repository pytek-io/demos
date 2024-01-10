"""
=========
Spy Demos
=========

Plot the sparsity pattern of arrays.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/spy_demos.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    np.random.seed(19680801)
    fig, axs = plt.subplots(2, 2)
    ax1 = axs[0, 0]
    ax2 = axs[0, 1]
    ax3 = axs[1, 0]
    ax4 = axs[1, 1]
    x = np.random.randn(20, 20)
    x[(5), :] = 0.0
    x[:, (12)] = 0.0
    ax1.spy(x, markersize=5)
    ax2.spy(x, precision=0.1, markersize=5)
    ax3.spy(x)
    ax4.spy(x, precision=0.1)
    return matplotlib_to_svg(fig)
