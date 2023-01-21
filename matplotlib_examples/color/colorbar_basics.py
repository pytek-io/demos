"""
========
Colorbar
========

Use `~.Figure.colorbar` by specifying the mappable object (here
the `.AxesImage` returned by `~.axes.Axes.imshow`)
and the axes to attach the colorbar to.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/color/colorbar_basics.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    N = 37
    x, y = np.mgrid[:N, :N]
    Z = np.cos(x * 0.2) + np.sin(y * 0.3)
    Zpos = np.ma.masked_less(Z, 0)
    Zneg = np.ma.masked_greater(Z, 0)
    fig, (ax1, ax2, ax3) = plt.subplots(figsize=(13, 3), ncols=3)
    pos = ax1.imshow(Zpos, cmap="Blues", interpolation="none")
    fig.colorbar(pos, ax=ax1)
    neg = ax2.imshow(Zneg, cmap="Reds_r", interpolation="none")
    fig.colorbar(neg, ax=ax2, location="right", anchor=(0, 0.3), shrink=0.7)
    pos_neg_clipped = ax3.imshow(
        Z, cmap="RdBu", vmin=-1.2, vmax=1.2, interpolation="none"
    )
    cbar = fig.colorbar(pos_neg_clipped, ax=ax3, extend="both")
    cbar.minorticks_on()
    return matplotlib_to_svg(fig)
