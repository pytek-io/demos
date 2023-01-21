"""
===========================
Frontpage histogram example
===========================

This example reproduces the frontpage histogram example.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/frontpage/histogram.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    random_state = np.random.RandomState(19680801)
    X = random_state.randn(10000)
    fig, ax = plt.subplots()
    ax.hist(X, bins=25, density=True)
    x = np.linspace(-5, 5, 1000)
    ax.plot(x, 1 / np.sqrt(2 * np.pi) * np.exp(-(x**2) / 2), linewidth=4)
    ax.set_xticks([])
    ax.set_yticks([])
    fig.savefig("histogram_frontpage.png", dpi=25)
    return matplotlib_to_svg(fig)
