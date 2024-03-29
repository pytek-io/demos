"""
==========
Hyperlinks
==========

This example demonstrates how to set a hyperlinks on various kinds of elements.

This currently only works with the SVG backend.


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/misc/hyperlinks_sgskip.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig = plt.figure()
    s = plt.scatter([1, 2, 3], [4, 5, 6])
    s.set_urls(["https://www.bbc.co.uk/news", "https://www.google.com/", None])
    fig.savefig("scatter.svg")
    fig = plt.figure()
    delta = 0.025
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-(X**2) - Y**2)
    Z2 = np.exp(-((X - 1) ** 2) - (Y - 1) ** 2)
    Z = (Z1 - Z2) * 2
    im = plt.imshow(
        Z, interpolation="bilinear", cmap=cm.gray, origin="lower", extent=[-3, 3, -3, 3]
    )
    im.set_url("https://www.google.com/")
    fig.savefig("image.svg")
    return matplotlib_to_svg(fig)
