"""
============
Axes Divider
============

Axes divider to calculate location of axes and
create a divider for them using existing axes instances.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/demo_axes_divider.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

from matplotlib import cbook
import matplotlib.pyplot as plt


def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy", np_load=True)
    return (z, ((-3), 4, (-4), 3))


def demo_simple_image(ax):
    (Z, extent) = get_demo_image()
    im = ax.imshow(Z, extent=extent)
    cb = plt.colorbar(im)
    cb.ax.yaxis.set_tick_params(labelright=False)


def demo_locatable_axes_hard(fig):
    from mpl_toolkits.axes_grid1 import SubplotDivider, Size
    from mpl_toolkits.axes_grid1.mpl_axes import Axes

    divider = SubplotDivider(fig, 2, 2, 2, aspect=True)
    ax = fig.add_axes(divider.get_position(), axes_class=Axes)
    ax_cb = fig.add_axes(divider.get_position(), axes_class=Axes, label="cb")
    h = [Size.AxesX(ax), Size.Fixed(0.05), Size.Fixed(0.2)]
    v = [Size.AxesY(ax)]
    divider.set_horizontal(h)
    divider.set_vertical(v)
    ax.set_axes_locator(divider.new_locator(nx=0, ny=0))
    ax_cb.set_axes_locator(divider.new_locator(nx=2, ny=0))
    ax_cb.axis["left"].toggle(all=False)
    ax_cb.axis["right"].toggle(ticks=True)
    (Z, extent) = get_demo_image()
    im = ax.imshow(Z, extent=extent)
    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.set_tick_params(labelright=False)


def demo_locatable_axes_easy(ax):
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    divider = make_axes_locatable(ax)
    ax_cb = divider.append_axes("right", size="5%", pad=0.05)
    fig = ax.get_figure()
    fig.add_axes(ax_cb)
    (Z, extent) = get_demo_image()
    im = ax.imshow(Z, extent=extent)
    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.tick_right()
    ax_cb.yaxis.set_tick_params(labelright=False)


def demo_images_side_by_side(ax):
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    divider = make_axes_locatable(ax)
    (Z, extent) = get_demo_image()
    ax2 = divider.append_axes("right", size="100%", pad=0.05)
    fig1 = ax.get_figure()
    fig1.add_axes(ax2)
    ax.imshow(Z, extent=extent)
    ax2.imshow(Z, extent=extent)
    ax2.yaxis.set_tick_params(labelleft=False)


def app():
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(2, 2, 1)
    demo_simple_image(ax)
    demo_locatable_axes_hard(fig)
    ax = fig.add_subplot(2, 2, 3)
    demo_locatable_axes_easy(ax)
    ax = fig.add_subplot(2, 2, 4)
    demo_images_side_by_side(ax)
    return matplotlib_to_svg(fig)
