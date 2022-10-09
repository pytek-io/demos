"""
====================
plot() format string
====================

Use a format string (here, 'ro') to set the color and markers of a
`~matplotlib.axes.Axes.plot`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/pyplot_formatstr.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt


def app():
    fig = plt.figure()
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")
    return matplotlib_to_svg(fig)
