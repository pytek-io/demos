"""
============
Pyplot Three
============

Plot three line plots in a single call to `~matplotlib.pyplot.plot`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/pyplot_three.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    t = np.arange(0.0, 5.0, 0.2)
    fig = plt.figure()
    plt.plot(t, t, "r--", t, t**2, "bs", t, t**3, "g^")
    return matplotlib_to_svg(fig)
