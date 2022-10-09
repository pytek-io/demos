"""
=====================
Simple Axes Divider 1
=====================

See also :doc:`/tutorials/toolkits/axes_grid`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/simple_axes_divider1.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

from mpl_toolkits.axes_grid1 import Size, Divider
import matplotlib.pyplot as plt


def label_axes(ax, text):
    """Place a label at the center of an Axes, and remove the axis ticks."""
    ax.text(
        0.5,
        0.5,
        text,
        transform=ax.transAxes,
        horizontalalignment="center",
        verticalalignment="center",
    )
    ax.tick_params(bottom=False, labelbottom=False, left=False, labelleft=False)


def app():
    fig = plt.figure(figsize=(6, 6))
    fig.suptitle("Fixed axes sizes, fixed paddings")
    horiz = [Size.Fixed(1.0), Size.Fixed(0.5), Size.Fixed(1.5), Size.Fixed(0.5)]
    vert = [Size.Fixed(1.5), Size.Fixed(0.5), Size.Fixed(1.0)]
    rect = (0.1, 0.1, 0.8, 0.8)
    div = Divider(fig, rect, horiz, vert, aspect=False)
    ax1 = fig.add_axes(rect, axes_locator=div.new_locator(nx=0, ny=0))
    label_axes(ax1, "nx=0, ny=0")
    ax2 = fig.add_axes(rect, axes_locator=div.new_locator(nx=0, ny=2))
    label_axes(ax2, "nx=0, ny=2")
    ax3 = fig.add_axes(rect, axes_locator=div.new_locator(nx=2, ny=2))
    label_axes(ax3, "nx=2, ny=2")
    ax4 = fig.add_axes(rect, axes_locator=div.new_locator(nx=2, nx1=4, ny=0))
    label_axes(ax4, "nx=2, nx1=4, ny=0")
    fig = plt.figure(figsize=(6, 6))
    fig.suptitle("Scalable axes sizes, fixed paddings")
    horiz = [Size.Scaled(1.5), Size.Fixed(0.5), Size.Scaled(1.0), Size.Scaled(0.5)]
    vert = [Size.Scaled(1.0), Size.Fixed(0.5), Size.Scaled(1.5)]
    rect = (0.1, 0.1, 0.8, 0.8)
    div = Divider(fig, rect, horiz, vert, aspect=False)
    ax1 = fig.add_axes(rect, axes_locator=div.new_locator(nx=0, ny=0))
    label_axes(ax1, "nx=0, ny=0")
    ax2 = fig.add_axes(rect, axes_locator=div.new_locator(nx=0, ny=2))
    label_axes(ax2, "nx=0, ny=2")
    ax3 = fig.add_axes(rect, axes_locator=div.new_locator(nx=2, ny=2))
    label_axes(ax3, "nx=2, ny=2")
    ax4 = fig.add_axes(rect, axes_locator=div.new_locator(nx=2, nx1=4, ny=0))
    label_axes(ax4, "nx=2, nx1=4, ny=0")
    return matplotlib_to_svg(fig)
