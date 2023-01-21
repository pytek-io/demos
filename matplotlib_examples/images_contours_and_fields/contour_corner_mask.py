"""
===================
Contour Corner Mask
===================

Illustrate the difference between ``corner_mask=False`` and
``corner_mask=True`` for masked contour plots.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/contour_corner_mask.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    x, y = np.meshgrid(np.arange(7), np.arange(10))
    z = np.sin(0.5 * x) * np.cos(0.52 * y)
    mask = np.zeros_like(z, dtype=bool)
    mask[(2), 3:5] = True
    mask[3:5, (4)] = True
    mask[7, 2] = True
    mask[5, 0] = True
    mask[0, 6] = True
    z = np.ma.array(z, mask=mask)
    corner_masks = [False, True]
    fig, axs = plt.subplots(ncols=2)
    for ax, corner_mask in zip(axs, corner_masks):
        cs = ax.contourf(x, y, z, corner_mask=corner_mask)
        ax.contour(cs, colors="k")
        ax.set_title("corner_mask = {0}".format(corner_mask))
        ax.grid(c="k", ls="-", alpha=0.3)
        ax.plot(np.ma.array(x, mask=~mask), y, "ro")
    return matplotlib_to_svg(fig)
