"""
==================================
Modifying the coordinate formatter
==================================

Modify the coordinate formatter to report the image "z"
value of the nearest pixel given x and y.
This functionality is built in by default, but it
is still useful to show how to customize the
`~.axes.Axes.format_coord` function.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/image_zcoord.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)
X = 10 * np.random.rand(5, 3)
(fig, ax) = plt.subplots()
ax.imshow(X)
(numrows, numcols) = X.shape


def format_coord(x, y):
    col = int((x + 0.5))
    row = int((y + 0.5))
    if (0 <= col < numcols) and (0 <= row < numrows):
        z = X[(row, col)]
        return "x=%1.4f, y=%1.4f, z=%1.4f" % (x, y, z)
    else:
        return "x=%1.4f, y=%1.4f" % (x, y)


def app():
    ax.format_coord = format_coord
    return matplotlib_to_svg(fig)
