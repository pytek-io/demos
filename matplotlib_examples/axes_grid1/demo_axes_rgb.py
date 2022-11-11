"""
==================================
Showing RGB channels using RGBAxes
==================================

`~.axes_grid1.axes_rgb.RGBAxes` creates a layout of 4 Axes for displaying RGB
channels: one large Axes for the RGB image and 3 smaller Axes for the R, G, B
channels.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/demo_axes_rgb.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
from matplotlib import cbook
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_rgb import make_rgb_axes, RGBAxes


def get_rgb():
    Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy", np_load=True)
    Z[(Z < 0)] = 0.0
    Z = Z / Z.max()
    R = Z[:13, :13]
    G = Z[2:, 2:]
    B = Z[:13, 2:]
    return (R, G, B)


def make_cube(r, g, b):
    (ny, nx) = r.shape
    R = np.zeros((ny, nx, 3))
    R[:, :, 0] = r
    G = np.zeros_like(R)
    G[:, :, 1] = g
    B = np.zeros_like(R)
    B[:, :, 2] = b
    RGB = (R + G) + B
    return (R, G, B, RGB)


def app():
    fig = plt.figure()
    ax = RGBAxes(fig, [0.1, 0.1, 0.8, 0.8], pad=0.0)
    (r, g, b) = get_rgb()
    ax.imshow_rgb(r, g, b)
    (fig, ax) = plt.subplots()
    (ax_r, ax_g, ax_b) = make_rgb_axes(ax, pad=0.02)
    (r, g, b) = get_rgb()
    (im_r, im_g, im_b, im_rgb) = make_cube(r, g, b)
    ax.imshow(im_rgb)
    ax_r.imshow(im_r)
    ax_g.imshow(im_g)
    ax_b.imshow(im_b)
    for ax in fig.axes:
        ax.tick_params(axis="both", direction="in")
        ax.spines[:].set_color("w")
        for tick in ax.xaxis.get_major_ticks() + ax.yaxis.get_major_ticks():
            tick.tick1line.set_markeredgecolor("w")
            tick.tick2line.set_markeredgecolor("w")
    return matplotlib_to_svg(fig)