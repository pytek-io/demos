"""
=====================
Grayscale style sheet
=====================

This example demonstrates the "grayscale" style sheet, which changes all colors
that are defined as `.rcParams` to grayscale. Note, however, that not all
plot elements respect `.rcParams`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/style_sheets/grayscale.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)


def color_cycle_example(ax):
    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams["axes.prop_cycle"])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin((x + s)), "o-")


def image_and_patch_example(ax):
    ax.imshow(np.random.random(size=(20, 20)), interpolation="none")
    c = plt.Circle((5, 5), radius=5, label="patch")
    ax.add_patch(c)


def app():
    plt.style.use("grayscale")
    (fig, (ax1, ax2)) = plt.subplots(ncols=2)
    fig.suptitle("'grayscale' style sheet")
    color_cycle_example(ax1)
    image_and_patch_example(ax2)
    return matplotlib_to_svg(fig)
