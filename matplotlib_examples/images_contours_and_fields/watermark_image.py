"""
===============
Watermark image
===============

Using a PNG file as a watermark.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/watermark_image.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib.pyplot as plt


def app():
    with cbook.get_sample_data("logo2.png") as file:
        im = image.imread(file)
    (fig, ax) = plt.subplots()
    ax.plot(np.sin((10 * np.linspace(0, 1))), "-o", ms=20, alpha=0.7, mfc="orange")
    ax.grid()
    fig.figimage(im, 10, 10, zorder=3, alpha=0.5)
    return matplotlib_to_svg(fig)
