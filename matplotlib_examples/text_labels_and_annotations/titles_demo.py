"""
=================
Title positioning
=================

Matplotlib can display plot titles centered, flush with the left side of
a set of axes, and flush with the right side of a set of axes.


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/text_labels_and_annotations/titles_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def app():
    plt.plot(range(10))
    plt.title("Center Title")
    plt.title("Left Title", loc="left")
    plt.title("Right Title", loc="right")
    fig, axs = plt.subplots(1, 2, constrained_layout=True)
    ax = axs[0]
    ax.plot(range(10))
    ax.xaxis.set_label_position("top")
    ax.set_xlabel("X-label")
    ax.set_title("Center Title")
    ax = axs[1]
    ax.plot(range(10))
    ax.xaxis.set_label_position("top")
    ax.xaxis.tick_top()
    ax.set_xlabel("X-label")
    ax.set_title("Center Title")
    fig, axs = plt.subplots(1, 2, constrained_layout=True)
    ax = axs[0]
    ax.plot(range(10))
    ax.xaxis.set_label_position("top")
    ax.set_xlabel("X-label")
    ax.set_title("Manual y", y=1.0, pad=-14)
    plt.rcParams["axes.titley"] = 1.0
    plt.rcParams["axes.titlepad"] = -14
    ax = axs[1]
    ax.plot(range(10))
    ax.set_xlabel("X-label")
    ax.set_title("rcParam y")
    return matplotlib_to_svg(fig)
