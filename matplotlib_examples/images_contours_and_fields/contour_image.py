"""
=============
Contour Image
=============

Test combinations of contouring, filled contouring, and image plotting.
For contour labelling, see also the :doc:`contour demo example
</gallery/images_contours_and_fields/contour_demo>`.

The emphasis in this demo is on showing how to make contours register
correctly on images, and on how to get both of them oriented as desired.
In particular, note the usage of the :doc:`"origin" and "extent"
</tutorials/intermediate/imshow_extent>` keyword arguments to imshow and
contour.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/contour_image.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

from demos.charts.utils import matplotlib_to_svg


def app():
    delta = 0.5
    extent = -3, 4, -4, 3
    x = np.arange(-3.0, 4.001, delta)
    y = np.arange(-4.0, 3.001, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-(X**2) - Y**2)
    Z2 = np.exp(-((X - 1) ** 2) - (Y - 1) ** 2)
    Z = (Z1 - Z2) * 2
    levels = np.arange(-2.0, 1.601, 0.4)
    norm = cm.colors.Normalize(vmax=abs(Z).max(), vmin=-abs(Z).max())
    cmap = cm.PRGn
    fig, _axs = plt.subplots(nrows=2, ncols=2)
    fig.subplots_adjust(hspace=0.3)
    axs = _axs.flatten()
    cset1 = axs[0].contourf(
        X, Y, Z, levels, norm=norm, cmap=cm.get_cmap(cmap, len(levels) - 1)
    )
    cset2 = axs[0].contour(X, Y, Z, cset1.levels, colors="k")
    for c in cset2.collections:
        c.set_linestyle("solid")
    cset3 = axs[0].contour(X, Y, Z, (0,), colors="g", linewidths=2)
    axs[0].set_title("Filled contours")
    fig.colorbar(cset1, ax=axs[0])
    axs[1].imshow(Z, extent=extent, cmap=cmap, norm=norm)
    axs[1].contour(Z, levels, colors="k", origin="upper", extent=extent)
    axs[1].set_title("Image, origin 'upper'")
    axs[2].imshow(Z, origin="lower", extent=extent, cmap=cmap, norm=norm)
    axs[2].contour(Z, levels, colors="k", origin="lower", extent=extent)
    axs[2].set_title("Image, origin 'lower'")
    im = axs[3].imshow(Z, interpolation="nearest", extent=extent, cmap=cmap, norm=norm)
    axs[3].contour(Z, levels, colors="k", origin="image", extent=extent)
    ylim = axs[3].get_ylim()
    axs[3].set_ylim(ylim[::-1])
    axs[3].set_title("Origin from rc, reversed y-axis")
    fig.colorbar(im, ax=axs[3])
    fig.tight_layout()
    return matplotlib_to_svg(fig)
