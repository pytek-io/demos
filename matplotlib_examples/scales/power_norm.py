"""
========================
Exploring normalizations
========================

Various normalization on a multivariate normal distribution.


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/scales/power_norm.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import multivariate_normal

from demos.charts.utils import matplotlib_to_svg


def app():
    np.random.seed(19680801)
    data = np.vstack(
        [
            multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
            multivariate_normal([30, 20], [[3, 1], [1, 3]], size=1000),
        ]
    )
    gammas = [0.8, 0.5, 0.3]
    fig, axs = plt.subplots(nrows=2, ncols=2)
    axs[0, 0].set_title("Linear normalization")
    axs[0, 0].hist2d(data[:, (0)], data[:, (1)], bins=100)
    for ax, gamma in zip(axs.flat[1:], gammas):
        ax.set_title("Power law $(\\gamma=%1.1f)$" % gamma)
        ax.hist2d(data[:, (0)], data[:, (1)], bins=100, norm=mcolors.PowerNorm(gamma))
    fig.tight_layout()
    return matplotlib_to_svg(fig)
