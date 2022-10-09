"""
==============================
Text Rotation Relative To Line
==============================

Text objects in matplotlib are normally rotated with respect to the
screen coordinate system (i.e., 45 degrees rotation plots text along a
line that is in between horizontal and vertical no matter how the axes
are changed).  However, at times one wants to rotate text with respect
to something on the plot.  In this case, the correct angle won't be
the angle of that object in the plot coordinate system, but the angle
that that object APPEARS in the screen coordinate system.  This angle
can be determined automatically by setting the parameter
*transform_rotates_text*, as shown in the example below.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/text_labels_and_annotations/text_rotation_relative_to_line.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import numpy as np


def app():
    (fig, ax) = plt.subplots()
    h = ax.plot(range(0, 10), range(0, 10))
    ax.set_xlim([(-10), 20])
    l1 = np.array((1, 1))
    l2 = np.array((5, 5))
    angle = 45
    th1 = ax.text(
        *l1,
        "text not rotated correctly",
        fontsize=16,
        rotation=angle,
        rotation_mode="anchor"
    )
    th2 = ax.text(
        *l2,
        "text rotated correctly",
        fontsize=16,
        rotation=angle,
        rotation_mode="anchor",
        transform_rotates_text=True
    )
    return matplotlib_to_svg(fig)
