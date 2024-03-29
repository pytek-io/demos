"""
===========
Symlog Demo
===========

Example use of symlog (symmetric log) axis scaling.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/scales/symlog_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    dt = 0.01
    x = np.arange(-50.0, 50.0, dt)
    y = np.arange(0, 100.0, dt)
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
    ax0.plot(x, y)
    ax0.set_xscale("symlog")
    ax0.set_ylabel("symlogx")
    ax0.grid()
    ax0.xaxis.grid(which="minor")
    ax1.plot(y, x)
    ax1.set_yscale("symlog")
    ax1.set_ylabel("symlogy")
    ax2.plot(x, np.sin(x / 3.0))
    ax2.set_xscale("symlog")
    ax2.set_yscale("symlog", linthresh=0.015)
    ax2.grid()
    ax2.set_ylabel("symlog both")
    fig.tight_layout()
    return matplotlib_to_svg(fig)
