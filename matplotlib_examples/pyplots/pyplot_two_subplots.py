"""
===================
Pyplot Two Subplots
===================

Create a figure with two subplots with `.pyplot.subplot`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/pyplot_two_subplots.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp((-t)) * np.cos(((2 * np.pi) * t))


def app():
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)
    fig = plt.figure()
    plt.subplot(211)
    plt.plot(t1, f(t1), color="tab:blue", marker="o")
    plt.plot(t2, f(t2), color="black")
    plt.subplot(212)
    plt.plot(t2, np.cos(((2 * np.pi) * t2)), color="tab:orange", linestyle="--")
    return matplotlib_to_svg(fig)
