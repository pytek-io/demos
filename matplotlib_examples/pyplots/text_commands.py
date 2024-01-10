"""
=============
Text Commands
=============

Plotting text of many different kinds.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/text_commands.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig = plt.figure()
    fig.suptitle("bold figure suptitle", fontsize=14, fontweight="bold")
    ax = fig.add_subplot()
    fig.subplots_adjust(top=0.85)
    ax.set_title("axes title")
    ax.set_xlabel("xlabel")
    ax.set_ylabel("ylabel")
    ax.text(
        3,
        8,
        "boxed italics text in data coords",
        style="italic",
        bbox={"facecolor": "red", "alpha": 0.5, "pad": 10},
    )
    ax.text(2, 6, "an equation: $E=mc^2$", fontsize=15)
    ax.text(3, 2, "Unicode: Institut für Festkörperphysik")
    ax.text(
        0.95,
        0.01,
        "colored text in axes coords",
        verticalalignment="bottom",
        horizontalalignment="right",
        transform=ax.transAxes,
        color="green",
        fontsize=15,
    )
    ax.plot([2], [1], "o")
    ax.annotate(
        "annotate",
        xy=(2, 1),
        xytext=(3, 4),
        arrowprops={"facecolor": "black", "shrink": 0.05},
    )
    ax.set(xlim=(0, 10), ylim=(0, 10))
    return matplotlib_to_svg(fig)
