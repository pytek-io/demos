"""
=======
Matshow
=======

`~.axes.Axes.matshow` visualizes a 2D matrix or array as color-coded image.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/matshow.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import numpy as np


def app():
    a = np.diag(range(15))
    fig = plt.matshow(a).figure
    return matplotlib_to_svg(fig)
