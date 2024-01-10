"""
============================
Colorbar with `.AxesDivider`
============================

The `.axes_divider.make_axes_locatable` function takes an existing axes, adds
it to a new `.AxesDivider` and returns the `.AxesDivider`.  The `.append_axes`
method of the `.AxesDivider` can then be used to create a new axes on a given
side ("top", "right", "bottom", or "left") of the original axes. This example
uses `.append_axes` to add colorbars next to axes.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/demo_colorbar_with_axes_divider.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.subplots_adjust(wspace=0.5)
    im1 = ax1.imshow([[1, 2], [3, 4]])
    ax1_divider = make_axes_locatable(ax1)
    cax1 = ax1_divider.append_axes("right", size="7%", pad="2%")
    cb1 = fig.colorbar(im1, cax=cax1)
    im2 = ax2.imshow([[1, 2], [3, 4]])
    ax2_divider = make_axes_locatable(ax2)
    cax2 = ax2_divider.append_axes("top", size="7%", pad="2%")
    cb2 = fig.colorbar(im2, cax=cax2, orientation="horizontal")
    cax2.xaxis.set_ticks_position("top")
    return matplotlib_to_svg(fig)
