"""
===========
Text Layout
===========

Create text with different alignment and rotation.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/text_layout.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as patches
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def app():
    fig = plt.figure()
    left, width = 0.25, 0.5
    bottom, height = 0.25, 0.5
    right = left + width
    top = bottom + height
    p = patches.Rectangle((left, bottom), width, height, fill=False)
    fig.add_artist(p)
    fig.text(
        left, bottom, "left top", horizontalalignment="left", verticalalignment="top"
    )
    fig.text(
        left,
        bottom,
        "left bottom",
        horizontalalignment="left",
        verticalalignment="bottom",
    )
    fig.text(
        right,
        top,
        "right bottom",
        horizontalalignment="right",
        verticalalignment="bottom",
    )
    fig.text(
        right, top, "right top", horizontalalignment="right", verticalalignment="top"
    )
    fig.text(
        right,
        bottom,
        "center top",
        horizontalalignment="center",
        verticalalignment="top",
    )
    fig.text(
        left,
        0.5 * (bottom + top),
        "right center",
        horizontalalignment="right",
        verticalalignment="center",
        rotation="vertical",
    )
    fig.text(
        left,
        0.5 * (bottom + top),
        "left center",
        horizontalalignment="left",
        verticalalignment="center",
        rotation="vertical",
    )
    fig.text(
        0.5 * (left + right),
        0.5 * (bottom + top),
        "middle",
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=20,
        color="red",
    )
    fig.text(
        right,
        0.5 * (bottom + top),
        "centered",
        horizontalalignment="center",
        verticalalignment="center",
        rotation="vertical",
    )
    fig.text(
        left,
        top,
        "rotated\nwith newlines",
        horizontalalignment="center",
        verticalalignment="center",
        rotation=45,
    )
    return matplotlib_to_svg(fig)
