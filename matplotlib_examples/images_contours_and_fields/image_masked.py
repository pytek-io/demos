"""
============
Image Masked
============

imshow with masked array input and out-of-range colors.

The second subplot illustrates the use of BoundaryNorm to
get a filled contour effect.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/image_masked.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors


def app():
    (x0, x1) = ((-5), 5)
    (y0, y1) = ((-3), 3)
    x = np.linspace(x0, x1, 500)
    y = np.linspace(y0, y1, 500)
    (X, Y) = np.meshgrid(x, y)
    Z1 = np.exp(((-(X**2)) - (Y**2)))
    Z2 = np.exp(((-((X - 1) ** 2)) - ((Y - 1) ** 2)))
    Z = (Z1 - Z2) * 2
    palette = plt.cm.gray.with_extremes(over="r", under="g", bad="b")
    Zm = np.ma.masked_where((Z > 1.2), Z)
    (fig, (ax1, ax2)) = plt.subplots(nrows=2, figsize=(6, 5.4))
    im = ax1.imshow(
        Zm,
        interpolation="bilinear",
        cmap=palette,
        norm=colors.Normalize(vmin=(-1.0), vmax=1.0),
        aspect="auto",
        origin="lower",
        extent=[x0, x1, y0, y1],
    )
    ax1.set_title("Green=low, Red=high, Blue=masked")
    cbar = fig.colorbar(im, extend="both", shrink=0.9, ax=ax1)
    cbar.set_label("uniform")
    for ticklabel in ax1.xaxis.get_ticklabels():
        ticklabel.set_visible(False)
    im = ax2.imshow(
        Zm,
        interpolation="nearest",
        cmap=palette,
        norm=colors.BoundaryNorm(
            [(-1), (-0.5), (-0.2), 0, 0.2, 0.5, 1], ncolors=palette.N
        ),
        aspect="auto",
        origin="lower",
        extent=[x0, x1, y0, y1],
    )
    ax2.set_title("With BoundaryNorm")
    cbar = fig.colorbar(im, extend="both", spacing="proportional", shrink=0.9, ax=ax2)
    cbar.set_label("proportional")
    fig.suptitle("imshow, with out-of-range and masked data")
    return matplotlib_to_svg(fig)
