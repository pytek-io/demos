"""
=============
Loglog Aspect
=============


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/scales/aspect_loglog.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_xscale("log")
    ax1.set_yscale("log")
    ax1.set_xlim(10.0, 1000.0)
    ax1.set_ylim(100.0, 1000.0)
    ax1.set_aspect(1)
    ax1.set_title("adjustable = box")
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_adjustable("datalim")
    ax2.plot([1, 3, 10], [1, 9, 100], "o-")
    ax2.set_xlim(0.1, 100.0)
    ax2.set_ylim(0.1, 1000.0)
    ax2.set_aspect(1)
    ax2.set_title("adjustable = datalim")
    return matplotlib_to_svg(fig)
