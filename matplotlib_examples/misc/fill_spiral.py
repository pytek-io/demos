"""
===========
Fill Spiral
===========


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/misc/fill_spiral.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig = plt.figure()
    theta = np.arange(0, 8 * np.pi, 0.1)
    a = 1
    b = 0.2
    for dt in np.arange(0, 2 * np.pi, np.pi / 2.0):
        x = a * np.cos(theta + dt) * np.exp(b * theta)
        y = a * np.sin(theta + dt) * np.exp(b * theta)
        dt = dt + np.pi / 4.0
        x2 = a * np.cos(theta + dt) * np.exp(b * theta)
        y2 = a * np.sin(theta + dt) * np.exp(b * theta)
        xf = np.concatenate((x, x2[::-1]))
        yf = np.concatenate((y, y2[::-1]))
        p1 = plt.fill(xf, yf)
    return matplotlib_to_svg(fig)
