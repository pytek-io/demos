"""
==================
Contour Label Demo
==================

Illustrate some of the more advanced things that one can do with
contour labels.

See also the :doc:`contour demo example
</gallery/images_contours_and_fields/contour_demo>`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/contour_label_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

from demos.charts.utils import matplotlib_to_svg

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-(X**2) - Y**2)
Z2 = np.exp(-((X - 1) ** 2) - (Y - 1) ** 2)
Z = (Z1 - Z2) * 2


def fmt_cb(x):
    s = f"{x:.1f}"
    if s.endswith("0"):
        s = f"{x:.0f}"
    return f"{s} \\%" if plt.rcParams["text.usetex"] else f"{s} %"


def app(_):
    fig, ax = plt.subplots()
    CS = ax.contour(X, Y, Z)
    ax.clabel(CS, CS.levels, inline=True, fmt=fmt_cb, fontsize=10)
    fig1, ax1 = plt.subplots()
    CS1 = ax1.contour(X, Y, Z)
    fmt = {}
    strs = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]
    for l, s in zip(CS1.levels, strs):
        fmt[l] = s
    ax1.clabel(CS1, CS1.levels[::2], inline=True, fmt=fmt, fontsize=10)
    fig2, ax2 = plt.subplots()
    CS2 = ax2.contour(X, Y, 100**Z, locator=plt.LogLocator())
    fmt = ticker.LogFormatterMathtext()
    fmt.create_dummy_axis()
    ax2.clabel(CS2, CS2.levels, fmt=fmt)
    ax2.set_title("$100^Z$")
    return matplotlib_to_svg(fig)
