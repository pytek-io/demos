"""
==============
Demo Axes Grid
==============

Grid of 2x2 images with single or own colorbar.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/demo_axes_grid.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid

from demos.charts.utils import matplotlib_to_svg


def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy", np_load=True)
    return z, (-3, 4, -4, 3)


def demo_simple_grid(fig):
    """
    A grid of 2x2 images with 0.05 inch pad between images and only
    the lower-left axes is labeled.
    """
    grid = ImageGrid(fig, 141, nrows_ncols=(2, 2), axes_pad=0.05, label_mode="1")
    Z, extent = get_demo_image()
    for ax in grid:
        ax.imshow(Z, extent=extent)
    grid.axes_llc.set_xticks([-2, 0, 2])
    grid.axes_llc.set_yticks([-2, 0, 2])


def demo_grid_with_single_cbar(fig):
    """
    A grid of 2x2 images with a single colorbar
    """
    grid = ImageGrid(
        fig,
        142,
        nrows_ncols=(2, 2),
        axes_pad=0.0,
        share_all=True,
        label_mode="L",
        cbar_location="top",
        cbar_mode="single",
    )
    Z, extent = get_demo_image()
    for ax in grid:
        im = ax.imshow(Z, extent=extent)
    grid.cbar_axes[0].colorbar(im)
    for cax in grid.cbar_axes:
        cax.toggle_label(False)
    grid.axes_llc.set_xticks([-2, 0, 2])
    grid.axes_llc.set_yticks([-2, 0, 2])


def demo_grid_with_each_cbar(fig):
    """
    A grid of 2x2 images. Each image has its own colorbar.
    """
    grid = ImageGrid(
        fig,
        143,
        nrows_ncols=(2, 2),
        axes_pad=0.1,
        label_mode="1",
        share_all=True,
        cbar_location="top",
        cbar_mode="each",
        cbar_size="7%",
        cbar_pad="2%",
    )
    Z, extent = get_demo_image()
    for ax, cax in zip(grid, grid.cbar_axes):
        im = ax.imshow(Z, extent=extent)
        cax.colorbar(im)
        cax.toggle_label(False)
    grid.axes_llc.set_xticks([-2, 0, 2])
    grid.axes_llc.set_yticks([-2, 0, 2])


def demo_grid_with_each_cbar_labelled(fig):
    """
    A grid of 2x2 images. Each image has its own colorbar.
    """
    grid = ImageGrid(
        fig,
        144,
        nrows_ncols=(2, 2),
        axes_pad=(0.45, 0.15),
        label_mode="1",
        share_all=True,
        cbar_location="right",
        cbar_mode="each",
        cbar_size="7%",
        cbar_pad="2%",
    )
    Z, extent = get_demo_image()
    limits = (0, 1), (-2, 2), (-1.7, 1.4), (-1.5, 1)
    for ax, cax, vlim in zip(grid, grid.cbar_axes, limits):
        im = ax.imshow(Z, extent=extent, vmin=vlim[0], vmax=vlim[1])
        cb = cax.colorbar(im)
        cb.set_ticks((vlim[0], vlim[1]))
    grid.axes_llc.set_xticks([-2, 0, 2])
    grid.axes_llc.set_yticks([-2, 0, 2])


def app(_):
    fig = plt.figure(figsize=(10.5, 2.5))
    fig.subplots_adjust(left=0.05, right=0.95)
    demo_simple_grid(fig)
    demo_grid_with_single_cbar(fig)
    demo_grid_with_each_cbar(fig)
    demo_grid_with_each_cbar_labelled(fig)
    return matplotlib_to_svg(fig)
