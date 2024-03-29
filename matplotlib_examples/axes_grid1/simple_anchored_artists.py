"""
=======================
Simple Anchored Artists
=======================

This example illustrates the use of the anchored helper classes found in
:mod:`matplotlib.offsetbox` and in :mod:`mpl_toolkits.axes_grid1`.
An implementation of a similar figure, but without use of the toolkit,
can be found in :doc:`/gallery/misc/anchored_artists`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/simple_anchored_artists.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def draw_text(ax):
    """
    Draw two text-boxes, anchored by different corners to the upper-left
    corner of the figure.
    """
    from matplotlib.offsetbox import AnchoredText

    at = AnchoredText("Figure 1a", loc="upper left", prop={"size": 8}, frameon=True)
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(at)
    at2 = AnchoredText(
        "Figure 1(b)",
        loc="lower left",
        prop={"size": 8},
        frameon=True,
        bbox_to_anchor=(0.0, 1.0),
        bbox_transform=ax.transAxes,
    )
    at2.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(at2)


def draw_circle(ax):
    """
    Draw a circle in axis coordinates
    """
    from matplotlib.patches import Circle
    from mpl_toolkits.axes_grid1.anchored_artists import AnchoredDrawingArea

    ada = AnchoredDrawingArea(20, 20, 0, 0, loc="upper right", pad=0.0, frameon=False)
    p = Circle((10, 10), 10)
    ada.da.add_artist(p)
    ax.add_artist(ada)


def draw_ellipse(ax):
    """
    Draw an ellipse of width=0.1, height=0.15 in data coordinates
    """
    from mpl_toolkits.axes_grid1.anchored_artists import AnchoredEllipse

    ae = AnchoredEllipse(
        ax.transData,
        width=0.1,
        height=0.15,
        angle=0.0,
        loc="lower left",
        pad=0.5,
        borderpad=0.4,
        frameon=True,
    )
    ax.add_artist(ae)


def draw_sizebar(ax):
    """
    Draw a horizontal bar with length of 0.1 in data coordinates,
    with a fixed label underneath.
    """
    from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar

    asb = AnchoredSizeBar(
        ax.transData,
        0.1,
        "1$^{\\prime}$",
        loc="lower center",
        pad=0.1,
        borderpad=0.5,
        sep=5,
        frameon=False,
    )
    ax.add_artist(asb)


def app(_):
    fig, ax = plt.subplots()
    ax.set_aspect(1.0)
    draw_text(ax)
    draw_circle(ax)
    draw_ellipse(ax)
    draw_sizebar(ax)
    return matplotlib_to_svg(fig)
