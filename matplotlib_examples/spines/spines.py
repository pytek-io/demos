"""
======
Spines
======

This demo compares:

- normal Axes, with spines on all four sides;
- an Axes with spines only on the left and bottom;
- an Axes using custom bounds to limit the extent of the spine.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/spines/spines.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    x = np.linspace(0, 2 * np.pi, 100)
    y = 2 * np.sin(x)
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, constrained_layout=True)
    ax0.plot(x, y)
    ax0.set_title("normal spines")
    ax1.plot(x, y)
    ax1.set_title("bottom-left spines")
    ax1.spines.right.set_visible(False)
    ax1.spines.top.set_visible(False)
    ax1.yaxis.set_ticks_position("left")
    ax1.xaxis.set_ticks_position("bottom")
    ax2.plot(x, y)
    ax2.spines.left.set_bounds(-1, 1)
    ax2.spines.right.set_visible(False)
    ax2.spines.top.set_visible(False)
    ax2.yaxis.set_ticks_position("left")
    ax2.xaxis.set_ticks_position("bottom")
    return matplotlib_to_svg(fig)
