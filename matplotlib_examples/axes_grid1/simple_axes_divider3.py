"""
=====================
Simple Axes Divider 3
=====================

See also :doc:`/tutorials/toolkits/axes_grid`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/simple_axes_divider3.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpl_toolkits.axes_grid1.axes_size as Size
from mpl_toolkits.axes_grid1 import Divider

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig = plt.figure(figsize=(5.5, 4))
    rect = 0.1, 0.1, 0.8, 0.8
    ax = [fig.add_axes(rect, label="%d" % i) for i in range(4)]
    horiz = [Size.AxesX(ax[0]), Size.Fixed(0.5), Size.AxesX(ax[1])]
    vert = [Size.AxesY(ax[0]), Size.Fixed(0.5), Size.AxesY(ax[2])]
    divider = Divider(fig, rect, horiz, vert, aspect=False)
    ax[0].set_axes_locator(divider.new_locator(nx=0, ny=0))
    ax[1].set_axes_locator(divider.new_locator(nx=2, ny=0))
    ax[2].set_axes_locator(divider.new_locator(nx=0, ny=2))
    ax[3].set_axes_locator(divider.new_locator(nx=2, ny=2))
    ax[0].set_xlim(0, 2)
    ax[1].set_xlim(0, 1)
    ax[0].set_ylim(0, 1)
    ax[2].set_ylim(0, 2)
    divider.set_aspect(1.0)
    for ax1 in ax:
        ax1.tick_params(labelbottom=False, labelleft=False)
    return matplotlib_to_svg(fig)
