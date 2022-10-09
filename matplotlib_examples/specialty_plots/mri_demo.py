"""
===
MRI
===

This example illustrates how to read an image (of an MRI) into a NumPy
array, and display it in greyscale using `~.axes.Axes.imshow`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/specialty_plots/mri_demo.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np


def app():
    with cbook.get_sample_data("s1045.ima.gz") as dfile:
        im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))
    (fig, ax) = plt.subplots(num="MRI_demo")
    ax.imshow(im, cmap="gray")
    ax.axis("off")
    return matplotlib_to_svg(fig)
