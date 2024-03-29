"""
===============
Simple Colorbar
===============


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/simple_colorbar.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig, ax = plt.subplots()
    im = ax.imshow(np.arange(100).reshape((10, 10)))
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(im, cax=cax)
    return matplotlib_to_svg(fig)
