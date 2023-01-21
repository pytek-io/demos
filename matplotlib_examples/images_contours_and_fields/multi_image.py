"""
===========
Multi Image
===========

Make a set of images with a single colormap, norm, and colorbar.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/multi_image.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

from demos.charts.utils import matplotlib_to_svg

np.random.seed(19680801)
Nr = 3
Nc = 2
fig, axs = plt.subplots(Nr, Nc)
fig.suptitle("Multiple images")
images = []
for i in range(Nr):
    for j in range(Nc):
        data = (1 + i + j) / 10 * np.random.rand(10, 20)
        images.append(axs[i, j].imshow(data))
        axs[i, j].label_outer()
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)
fig.colorbar(images[0], ax=axs, orientation="horizontal", fraction=0.1)


def update(changed_image):
    for im in images:
        if (
            changed_image.get_cmap() != im.get_cmap()
            or changed_image.get_clim() != im.get_clim()
        ):
            im.set_cmap(changed_image.get_cmap())
            im.set_clim(changed_image.get_clim())


def app():
    for im in images:
        im.callbacks.connect("changed", update)
    return matplotlib_to_svg(fig)
