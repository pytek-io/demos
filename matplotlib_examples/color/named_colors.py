"""
====================
List of named colors
====================

This plots a list of the named colors supported in matplotlib.
For more information on colors in matplotlib see

* the :doc:`/tutorials/colors/colors` tutorial;
* the `matplotlib.colors` API;
* the :doc:`/gallery/color/color_demo`.

----------------------------
Helper Function for Plotting
----------------------------
First we define a helper function for making a table of colors, then we use it
on some common color categories.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/color/named_colors.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from demos.charts.utils import matplotlib_to_svg


def plot_colortable(colors, sort_colors=True, emptycols=0):
    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12
    if sort_colors is True:
        by_hsv = sorted(
            (tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(color))), name)
            for name, color in colors.items()
        )
        names = [name for hsv, name in by_hsv]
    else:
        names = list(colors)
    n = len(names)
    ncols = 4 - emptycols
    nrows = n // ncols + int(n % ncols > 0)
    width = cell_width * 4 + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72
    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(
        margin / width,
        margin / height,
        (width - margin) / width,
        (height - margin) / height,
    )
    ax.set_xlim(0, cell_width * 4)
    ax.set_ylim(cell_height * (nrows - 0.5), -cell_height / 2.0)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()
    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height
        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7
        ax.text(
            text_pos_x,
            y,
            name,
            fontsize=14,
            horizontalalignment="left",
            verticalalignment="center",
        )
        ax.add_patch(
            Rectangle(
                xy=(swatch_start_x, y - 9),
                width=swatch_width,
                height=18,
                facecolor=colors[name],
                edgecolor="0.7",
            )
        )
    return fig


def app(_):
    plot_colortable(mcolors.BASE_COLORS, sort_colors=False, emptycols=1)
    plot_colortable(mcolors.TABLEAU_COLORS, sort_colors=False, emptycols=2)
    fig = plot_colortable(mcolors.CSS4_COLORS)
    return matplotlib_to_svg(fig)
