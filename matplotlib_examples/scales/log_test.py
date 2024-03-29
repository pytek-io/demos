"""
========
Log Axis
========

This is an example of assigning a log-scale for the x-axis using
`~.axes.Axes.semilogx`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/scales/log_test.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig, ax = plt.subplots()
    dt = 0.01
    t = np.arange(dt, 20.0, dt)
    ax.semilogx(t, np.exp(-t / 5.0))
    ax.grid()
    return matplotlib_to_svg(fig)
