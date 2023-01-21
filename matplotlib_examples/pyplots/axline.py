"""
==============
Infinite lines
==============

`~.axes.Axes.axvline` and `~.axes.Axes.axhline` draw infinite vertical /
horizontal lines, at given *x* / *y* positions. They are usually used to mark
special data values, e.g. in this example the center and limit values of the
sigmoid function.

`~.axes.Axes.axline` draws infinite straight lines in arbitrary directions.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/axline.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    t = np.linspace(-10, 10, 100)
    sig = 1 / (1 + np.exp(-t))
    fig = plt.figure()
    plt.axhline(y=0, color="black", linestyle="--")
    plt.axhline(y=0.5, color="black", linestyle=":")
    plt.axhline(y=1.0, color="black", linestyle="--")
    plt.axvline(color="grey")
    plt.axline((0, 0.5), slope=0.25, color="black", linestyle=(0, (5, 5)))
    plt.plot(t, sig, linewidth=2, label="$\\sigma(t) = \\frac{1}{1 + e^{-t}}$")
    plt.xlim(-10, 10)
    plt.xlabel("t")
    plt.legend(fontsize=14)
    for pos in np.linspace(-2, 1, 10):
        plt.axline((pos, 0), slope=0.5, color="k", transform=plt.gca().transAxes)
    plt.ylim([0, 1])
    plt.xlim([0, 1])
    return matplotlib_to_svg(fig)
