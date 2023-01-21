"""
======
Scales
======

Illustrate the scale transformations applied to axes, e.g. log, symlog, logit.

The last two examples are examples of using the ``'function'`` scale by
supplying forward and inverse functions for the scale transformation.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/scales/scales.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FixedLocator, NullFormatter

from demos.charts.utils import matplotlib_to_svg

np.random.seed(19680801)
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))
fig, axs = plt.subplots(3, 2, figsize=(6, 8), constrained_layout=True)
ax = axs[0, 0]
ax.plot(x, y)
ax.set_yscale("linear")
ax.set_title("linear")
ax.grid(True)
ax = axs[0, 1]
ax.plot(x, y)
ax.set_yscale("log")
ax.set_title("log")
ax.grid(True)
ax = axs[1, 1]
ax.plot(x, y - y.mean())
ax.set_yscale("symlog", linthresh=0.02)
ax.set_title("symlog")
ax.grid(True)
ax = axs[1, 0]
ax.plot(x, y)
ax.set_yscale("logit")
ax.set_title("logit")
ax.grid(True)


def forward(x):
    return x ** (1 / 2)


def inverse(x):
    return x**2


ax = axs[2, 0]
ax.plot(x, y)
ax.set_yscale("function", functions=(forward, inverse))
ax.set_title("function: $x^{1/2}$")
ax.grid(True)
ax.yaxis.set_major_locator(FixedLocator(np.arange(0, 1, 0.2) ** 2))
ax.yaxis.set_major_locator(FixedLocator(np.arange(0, 1, 0.2)))


def forward(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.log(np.abs(np.tan(a) + 1.0 / np.cos(a))))


def inverse(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.arctan(np.sinh(a)))


def app():
    ax = axs[2, 1]
    t = np.arange(0, 170.0, 0.1)
    s = t / 2.0
    ax.plot(t, s, "-", lw=2)
    ax.set_yscale("function", functions=(forward, inverse))
    ax.set_title("function: Mercator")
    ax.grid(True)
    ax.set_xlim([0, 180])
    ax.yaxis.set_minor_formatter(NullFormatter())
    ax.yaxis.set_major_locator(FixedLocator(np.arange(0, 90, 10)))
    return matplotlib_to_svg(fig)
