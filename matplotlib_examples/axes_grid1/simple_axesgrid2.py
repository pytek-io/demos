"""
==================
Simple ImageGrid 2
==================

Align multiple images of different sizes using
`~mpl_toolkits.axes_grid1.axes_grid.ImageGrid`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/simple_axesgrid2.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

from matplotlib import cbook
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid


def app():
    fig = plt.figure(figsize=(5.5, 3.5))
    grid = ImageGrid(fig, 111, nrows_ncols=(1, 3), axes_pad=0.1, label_mode="L")
    Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy", np_load=True)
    im1 = Z
    im2 = Z[:, :10]
    im3 = Z[:, 10:]
    (vmin, vmax) = (Z.min(), Z.max())
    for (ax, im) in zip(grid, [im1, im2, im3]):
        ax.imshow(im, origin="lower", vmin=vmin, vmax=vmax)
    return matplotlib_to_svg(fig)
