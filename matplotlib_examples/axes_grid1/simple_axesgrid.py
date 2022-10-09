"""
================
Simple ImageGrid
================

Align multiple images using `~mpl_toolkits.axes_grid1.axes_grid.ImageGrid`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/simple_axesgrid.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np


def app():
    im1 = np.arange(100).reshape((10, 10))
    im2 = im1.T
    im3 = np.flipud(im1)
    im4 = np.fliplr(im2)
    fig = plt.figure(figsize=(4.0, 4.0))
    grid = ImageGrid(fig, 111, nrows_ncols=(2, 2), axes_pad=0.1)
    for (ax, im) in zip(grid, [im1, im2, im3, im4]):
        ax.imshow(im)
    return matplotlib_to_svg(fig)
