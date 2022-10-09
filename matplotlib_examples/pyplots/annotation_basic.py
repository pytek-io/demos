"""
=================
Annotating a plot
=================

This example shows how to annotate a plot with an arrow pointing to provided
coordinates. We modify the defaults of the arrow, to "shrink" it.

For a complete overview of the annotation capabilities, also see the
:doc:`annotation tutorial</tutorials/text/annotations>`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/annotation_basic.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def app():
    (fig, ax) = plt.subplots()
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(((2 * np.pi) * t))
    (line,) = ax.plot(t, s, lw=2)
    ax.annotate(
        "local max",
        xy=(2, 1),
        xytext=(3, 1.5),
        arrowprops=dict(facecolor="black", shrink=0.05),
    )
    ax.set_ylim((-2), 2)
    return matplotlib_to_svg(fig)
