"""
=====================
Major and minor ticks
=====================

Demonstrate how to use major and minor tickers.

The two relevant classes are `.Locator`\s and `.Formatter`\s.  Locators
determine where the ticks are, and formatters control the formatting of tick
labels.

Minor ticks are off by default (using `.NullLocator` and `.NullFormatter`).
Minor ticks can be turned on without labels by setting the minor locator.
Minor tick labels can be turned on by setting the minor formatter.

`.MultipleLocator` places ticks on multiples of some base.
`.StrMethodFormatter` uses a format string (e.g., ``'{x:d}'`` or ``'{x:1.2f}'``
or ``'{x:1.1f} cm'``) to format the tick labels (the variable in the format
string must be ``'x'``).  For a `.StrMethodFormatter`, the string can be passed
directly to `.Axis.set_major_formatter` or
`.Axis.set_minor_formatter`.  An appropriate `.StrMethodFormatter` will
be created and used automatically.

`.pyplot.grid` changes the grid settings of the major ticks of the y and y axis
together.  If you want to control the grid of the minor ticks for a given axis,
use for example ::

  ax.xaxis.grid(True, which='minor')

Note that a given locator or formatter instance can only be used on a single
axis (because the locator stores references to the axis data and view limits).

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/ticks/major_minor_demo.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, AutoMinorLocator


def app():
    t = np.arange(0.0, 100.0, 0.1)
    s = np.sin(((0.1 * np.pi) * t)) * np.exp(((-t) * 0.01))
    (fig, ax) = plt.subplots()
    ax.plot(t, s)
    ax.xaxis.set_major_locator(MultipleLocator(20))
    ax.xaxis.set_major_formatter("{x:.0f}")
    ax.xaxis.set_minor_locator(MultipleLocator(5))
    t = np.arange(0.0, 100.0, 0.01)
    s = np.sin(((2 * np.pi) * t)) * np.exp(((-t) * 0.01))
    (fig, ax) = plt.subplots()
    ax.plot(t, s)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which="both", width=2)
    ax.tick_params(which="major", length=7)
    ax.tick_params(which="minor", length=4, color="r")
    return matplotlib_to_svg(fig)
