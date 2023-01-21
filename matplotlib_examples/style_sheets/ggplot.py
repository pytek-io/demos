"""
==================
ggplot style sheet
==================

This example demonstrates the "ggplot" style, which adjusts the style to
emulate ggplot_ (a popular plotting package for R_).

These settings were shamelessly stolen from [1]_ (with permission).

.. [1] https://everyhue.me/posts/sane-color-scheme-for-matplotlib/

.. _ggplot: https://ggplot2.tidyverse.org/
.. _R: https://www.r-project.org/


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/style_sheets/ggplot.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    plt.style.use("ggplot")
    np.random.seed(19680801)
    fig, axs = plt.subplots(ncols=2, nrows=2)
    ax1, ax2, ax3, ax4 = axs.flat
    x, y = np.random.normal(size=(2, 200))
    ax1.plot(x, y, "o")
    L = 2 * np.pi
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams["axes.prop_cycle"])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax2.plot(x, np.sin(x + s), "-")
    ax2.margins(0)
    x = np.arange(5)
    y1, y2 = np.random.randint(1, 25, size=(2, 5))
    width = 0.25
    ax3.bar(x, y1, width)
    ax3.bar(
        x + width, y2, width, color=list(plt.rcParams["axes.prop_cycle"])[2]["color"]
    )
    ax3.set_xticks(x + width, labels=["a", "b", "c", "d", "e"])
    for i, color in enumerate(plt.rcParams["axes.prop_cycle"]):
        xy = np.random.normal(size=2)
        ax4.add_patch(plt.Circle(xy, radius=0.3, color=color["color"]))
    ax4.axis("equal")
    ax4.margins(0)
    return matplotlib_to_svg(fig)
