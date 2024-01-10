"""
============================
Clipping images with patches
============================

Demo of image that's been clipped by a circular patch.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/image_clip_path.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.cbook as cbook
import matplotlib.patches as patches
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def app(_):
    with cbook.get_sample_data("grace_hopper.jpg") as image_file:
        image = plt.imread(image_file)
    fig, ax = plt.subplots()
    im = ax.imshow(image)
    patch = patches.Circle((260, 200), radius=200, transform=ax.transData)
    im.set_clip_path(patch)
    ax.axis("off")
    return matplotlib_to_svg(fig)
