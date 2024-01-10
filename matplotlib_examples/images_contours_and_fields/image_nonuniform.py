"""
================
Image Nonuniform
================

This illustrates the NonUniformImage class.  It is not
available via an Axes method but it is easily added to an
Axes instance as shown here.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/image_nonuniform.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.image import NonUniformImage

from demos.charts.utils import matplotlib_to_svg


def app(_):
    interp = "nearest"
    x = np.linspace(-4, 4, 9)
    x2 = x**3
    y = np.linspace(-4, 4, 9)
    z = np.sqrt(x[(np.newaxis), :] ** 2 + y[:, (np.newaxis)] ** 2)
    fig, axs = plt.subplots(nrows=2, ncols=2, constrained_layout=True)
    fig.suptitle("NonUniformImage class", fontsize="large")
    ax = axs[0, 0]
    im = NonUniformImage(
        ax, interpolation=interp, extent=(-4, 4, -4, 4), cmap=cm.Purples
    )
    im.set_data(x, y, z)
    ax.add_image(im)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_title(interp)
    ax = axs[0, 1]
    im = NonUniformImage(
        ax, interpolation=interp, extent=(-64, 64, -4, 4), cmap=cm.Purples
    )
    im.set_data(x2, y, z)
    ax.add_image(im)
    ax.set_xlim(-64, 64)
    ax.set_ylim(-4, 4)
    ax.set_title(interp)
    interp = "bilinear"
    ax = axs[1, 0]
    im = NonUniformImage(
        ax, interpolation=interp, extent=(-4, 4, -4, 4), cmap=cm.Purples
    )
    im.set_data(x, y, z)
    ax.add_image(im)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_title(interp)
    ax = axs[1, 1]
    im = NonUniformImage(
        ax, interpolation=interp, extent=(-64, 64, -4, 4), cmap=cm.Purples
    )
    im.set_data(x2, y, z)
    ax.add_image(im)
    ax.set_xlim(-64, 64)
    ax.set_ylim(-4, 4)
    ax.set_title(interp)
    return matplotlib_to_svg(fig)
