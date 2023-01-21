"""
===========================
Dark background style sheet
===========================

This example demonstrates the "dark_background" style, which uses white for
elements that are typically black (text, borders, etc). Note that not all plot
elements default to colors defined by an rc parameter.


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/style_sheets/dark_background.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    plt.style.use("dark_background")
    fig, ax = plt.subplots()
    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams["axes.prop_cycle"])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), "o-")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_title("'dark_background' style sheet")
    return matplotlib_to_svg(fig)
