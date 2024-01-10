"""
================
Color by y-value
================

Use masked arrays to plot a line with different colors by y-value.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/color/color_by_yvalue.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    t = np.arange(0.0, 2.0, 0.01)
    s = np.sin(2 * np.pi * t)
    upper = 0.77
    lower = -0.77
    supper = np.ma.masked_where(s < upper, s)
    slower = np.ma.masked_where(s > lower, s)
    smiddle = np.ma.masked_where((s < lower) | (s > upper), s)
    fig, ax = plt.subplots()
    ax.plot(t, smiddle, t, slower, t, supper)
    return matplotlib_to_svg(fig)
