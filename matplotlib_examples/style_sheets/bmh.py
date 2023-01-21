"""
========================================
Bayesian Methods for Hackers style sheet
========================================

This example demonstrates the style used in the Bayesian Methods for Hackers
[1]_ online book.

.. [1] http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/style_sheets/bmh.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg

np.random.seed(19680801)
plt.style.use("bmh")


def plot_beta_hist(ax, a, b):
    ax.hist(
        np.random.beta(a, b, size=10000),
        histtype="stepfilled",
        bins=25,
        alpha=0.8,
        density=True,
    )


def app():
    fig, ax = plt.subplots()
    plot_beta_hist(ax, 10, 10)
    plot_beta_hist(ax, 4, 12)
    plot_beta_hist(ax, 50, 12)
    plot_beta_hist(ax, 6, 55)
    ax.set_title("'bmh' style sheet")
    return matplotlib_to_svg(fig)
