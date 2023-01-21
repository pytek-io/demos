"""
=============
Pyplot Simple
=============

A very simple pyplot where a list of numbers are plotted against their
index. Creates a straight line due to the rate of change being 1 for
both the X and Y axis.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/pyplot_simple.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def app():
    fig = plt.figure()
    plt.plot([1, 2, 3, 4])
    plt.ylabel("some numbers")
    return matplotlib_to_svg(fig)
