"""
=============
Figimage Demo
=============

This illustrates placing images directly in the figure, with no Axes objects.


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/figimage_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    fig = plt.figure()
    Z = np.arange(10000).reshape((100, 100))
    Z[:, 50:] = 1
    im1 = fig.figimage(Z, xo=50, yo=0, origin="lower")
    im2 = fig.figimage(Z, xo=100, yo=100, alpha=0.8, origin="lower")
    return matplotlib_to_svg(fig)
