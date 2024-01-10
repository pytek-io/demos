"""
===================
Custom spine bounds
===================

Demo of spines using custom bounds to limit the extent of the spine.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/spines/spines_bounds.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    np.random.seed(19680801)
    x = np.linspace(0, 2 * np.pi, 50)
    y = np.sin(x)
    y2 = y + 0.1 * np.random.normal(size=x.shape)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(x, y2)
    ax.set_xlim((0, 2 * np.pi))
    ax.set_xticks([0, np.pi, 2 * np.pi], labels=["0", "$\\pi$", "2$\\pi$"])
    ax.set_ylim((-1.5, 1.5))
    ax.set_yticks([-1, 0, 1])
    ax.spines.left.set_bounds((-1, 1))
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.yaxis.set_ticks_position("left")
    ax.xaxis.set_ticks_position("bottom")
    return matplotlib_to_svg(fig)
