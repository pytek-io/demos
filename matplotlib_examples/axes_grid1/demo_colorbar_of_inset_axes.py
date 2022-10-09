"""
===============================
Adding a colorbar to inset axes
===============================

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/demo_colorbar_of_inset_axes.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

from matplotlib import cbook
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes


def app():
    (fig, ax) = plt.subplots(figsize=[5, 4])
    ax.set(aspect=1, xlim=((-15), 15), ylim=((-20), 5))
    Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy", np_load=True)
    extent = ((-3), 4, (-4), 3)
    axins = zoomed_inset_axes(ax, zoom=2, loc="upper left")
    axins.set(xticks=[], yticks=[])
    im = axins.imshow(Z, extent=extent, origin="lower")
    cax = inset_axes(
        axins,
        width="5%",
        height="100%",
        loc="lower left",
        bbox_to_anchor=(1.05, 0.0, 1, 1),
        bbox_transform=axins.transAxes,
        borderpad=0,
    )
    fig.colorbar(im, cax=cax)
    return matplotlib_to_svg(fig)
