"""
==============
BboxImage Demo
==============

A `~matplotlib.image.BboxImage` can be used to position an image according to
a bounding box. This demo shows how to show an image inside a `.text.Text`'s
bounding box as well as how to manually create a bounding box for the image.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/demo_bboximage.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import BboxImage
from matplotlib.transforms import Bbox, TransformedBbox


def app():
    (fig, (ax1, ax2)) = plt.subplots(ncols=2)
    txt = ax1.text(0.5, 0.5, "test", size=30, ha="center", color="w")
    kwargs = dict()
    bbox_image = BboxImage(
        txt.get_window_extent, norm=None, origin=None, clip_on=False, **kwargs
    )
    a = np.arange(256).reshape(1, 256) / 256.0
    bbox_image.set_data(a)
    ax1.add_artist(bbox_image)
    a = np.linspace(0, 1, 256).reshape(1, (-1))
    a = np.vstack((a, a))
    cmap_names = sorted((m for m in plt.colormaps if (not m.endswith("_r"))))
    ncol = 2
    nrow = (len(cmap_names) // ncol) + 1
    xpad_fraction = 0.3
    dx = 1 / (ncol + (xpad_fraction * (ncol - 1)))
    ypad_fraction = 0.3
    dy = 1 / (nrow + (ypad_fraction * (nrow - 1)))
    for (i, cmap_name) in enumerate(cmap_names):
        (ix, iy) = divmod(i, nrow)
        bbox0 = Bbox.from_bounds(
            ((ix * dx) * (1 + xpad_fraction)),
            ((1.0 - ((iy * dy) * (1 + ypad_fraction))) - dy),
            dx,
            dy,
        )
        bbox = TransformedBbox(bbox0, ax2.transAxes)
        bbox_image = BboxImage(bbox, cmap=cmap_name, norm=None, origin=None, **kwargs)
        bbox_image.set_data(a)
        ax2.add_artist(bbox_image)
    return matplotlib_to_svg(fig)
