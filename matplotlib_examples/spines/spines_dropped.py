"""
==============
Dropped spines
==============

Demo of spines offset from the axes (a.k.a. "dropped spines").

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/spines/spines_dropped.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def app():
    np.random.seed(19680801)
    (fig, ax) = plt.subplots()
    image = np.random.uniform(size=(10, 10))
    ax.imshow(image, cmap=plt.cm.gray)
    ax.set_title("dropped spines")
    ax.spines.left.set_position(("outward", 10))
    ax.spines.bottom.set_position(("outward", 10))
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.yaxis.set_ticks_position("left")
    ax.xaxis.set_ticks_position("bottom")
    return matplotlib_to_svg(fig)
