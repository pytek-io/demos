"""
===========
Pyplot Text
===========


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/pyplot_text.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    np.random.seed(19680801)
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)
    n, bins, patches = plt.hist(x, 50, density=True, facecolor="g", alpha=0.75)
    fig = plt.figure()
    plt.xlabel("Smarts")
    plt.ylabel("Probability")
    plt.title("Histogram of IQ")
    plt.text(60, 0.025, "$\\mu=100,\\ \\sigma=15$")
    plt.xlim(40, 160)
    plt.ylim(0, 0.03)
    plt.grid(True)
    return matplotlib_to_svg(fig)
