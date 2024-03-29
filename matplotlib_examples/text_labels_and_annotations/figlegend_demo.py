"""
==================
Figure legend demo
==================

Instead of plotting a legend on each axis, a legend for all the artists on all
the sub-axes of a figure can be plotted instead.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/text_labels_and_annotations/figlegend_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig, axs = plt.subplots(1, 2)
    x = np.arange(0.0, 2.0, 0.02)
    y1 = np.sin(2 * np.pi * x)
    y2 = np.exp(-x)
    (l1,) = axs[0].plot(x, y1)
    (l2,) = axs[0].plot(x, y2, marker="o")
    y3 = np.sin(4 * np.pi * x)
    y4 = np.exp(-2 * x)
    (l3,) = axs[1].plot(x, y3, color="tab:green")
    (l4,) = axs[1].plot(x, y4, color="tab:red", marker="^")
    fig.legend((l1, l2), ("Line 1", "Line 2"), "upper left")
    fig.legend((l3, l4), ("Line 3", "Line 4"), "upper right")
    plt.tight_layout()
    return matplotlib_to_svg(fig)
