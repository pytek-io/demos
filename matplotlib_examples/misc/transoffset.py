"""
======================
transforms.offset_copy
======================

This illustrates the use of `.transforms.offset_copy` to
make a transform that positions a drawing element such as
a text string at a specified offset in screen coordinates
(dots or inches) relative to a location given in any
coordinates.

Every Artist (Text, Line2D, etc.) has a transform that can be
set when the Artist is created, such as by the corresponding
pyplot function.  By default this is usually the Axes.transData
transform, going from data units to screen pixels.  We can
use the `.offset_copy` function to make a modified copy of
this transform, where the modification consists of an
offset.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/misc/transoffset.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import numpy as np


def app():
    xs = np.arange(7)
    ys = xs**2
    fig = plt.figure(figsize=(5, 10))
    ax = plt.subplot(2, 1, 1)
    trans_offset = mtransforms.offset_copy(
        ax.transData, fig=fig, x=0.05, y=0.1, units="inches"
    )
    for (x, y) in zip(xs, ys):
        plt.plot(x, y, "ro")
        plt.text(x, y, ("%d, %d" % (int(x), int(y))), transform=trans_offset)
    ax = plt.subplot(2, 1, 2, projection="polar")
    trans_offset = mtransforms.offset_copy(ax.transData, fig=fig, y=6, units="dots")
    for (x, y) in zip(xs, ys):
        plt.polar(x, y, "ro")
        plt.text(
            x,
            y,
            ("%d, %d" % (int(x), int(y))),
            transform=trans_offset,
            horizontalalignment="center",
            verticalalignment="bottom",
        )
    return matplotlib_to_svg(fig)
