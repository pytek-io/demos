"""
================
Simple Axisline4
================


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/simple_axisline4.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import host_subplot

from demos.charts.utils import matplotlib_to_svg


def app():
    fig = plt.figure()
    ax = host_subplot(111, figure=fig)
    xx = np.arange(0, 2 * np.pi, 0.01)
    ax.plot(xx, np.sin(xx))
    ax2 = ax.twin()
    ax2.set_xticks(
        [0.0, 0.5 * np.pi, np.pi, 1.5 * np.pi, 2 * np.pi],
        labels=["$0$", "$\\frac{1}{2}\\pi$", "$\\pi$", "$\\frac{3}{2}\\pi$", "$2\\pi$"],
    )
    ax2.axis["right"].major_ticklabels.set_visible(False)
    ax2.axis["top"].major_ticklabels.set_visible(True)
    return matplotlib_to_svg(fig)
