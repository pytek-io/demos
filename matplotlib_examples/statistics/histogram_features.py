"""
==============================================
Some features of the histogram (hist) function
==============================================

In addition to the basic histogram, this demo shows a few optional features:

* Setting the number of data bins.
* The *density* parameter, which normalizes bin heights so that the integral of
  the histogram is 1. The resulting histogram is an approximation of the
  probability density function.

Selecting different bin counts and sizes can significantly affect the shape
of a histogram. The Astropy docs have a great section_ on how to select these
parameters.

.. _section: http://docs.astropy.org/en/stable/visualization/histogram.html

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/statistics/histogram_features.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    np.random.seed(19680801)
    mu = 100
    sigma = 15
    x = mu + sigma * np.random.randn(437)
    num_bins = 50
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(x, num_bins, density=True)
    y = 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2)
    ax.plot(bins, y, "--")
    ax.set_xlabel("Smarts")
    ax.set_ylabel("Probability density")
    ax.set_title("Histogram of IQ: $\\mu=100$, $\\sigma=15$")
    fig.tight_layout()
    return matplotlib_to_svg(fig)
