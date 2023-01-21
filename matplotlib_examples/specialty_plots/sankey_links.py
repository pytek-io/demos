"""
======================================
Long chain of connections using Sankey
======================================

Demonstrate/test the Sankey class by producing a long chain of connections.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/specialty_plots/sankey_links.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

from demos.charts.utils import matplotlib_to_svg

links_per_side = 6


def side(sankey, n=1):
    """Generate a side chain."""
    prior = len(sankey.diagrams)
    for i in range(0, 2 * n, 2):
        sankey.add(
            flows=[1, -1],
            orientations=[-1, -1],
            patchlabel=str(prior + i),
            prior=prior + i - 1,
            connect=(1, 0),
            alpha=0.5,
        )
        sankey.add(
            flows=[1, -1],
            orientations=[1, 1],
            patchlabel=str(prior + i + 1),
            prior=prior + i,
            connect=(1, 0),
            alpha=0.5,
        )


def corner(sankey):
    """Generate a corner link."""
    prior = len(sankey.diagrams)
    sankey.add(
        flows=[1, -1],
        orientations=[0, 1],
        patchlabel=str(prior),
        facecolor="k",
        prior=prior - 1,
        connect=(1, 0),
        alpha=0.5,
    )


def app():
    fig = plt.figure()
    ax = fig.add_subplot(
        1,
        1,
        1,
        xticks=[],
        yticks=[],
        title="""Why would you want to do this?
(But you could.)""",
    )
    sankey = Sankey(ax=ax, unit=None)
    sankey.add(
        flows=[1, -1], orientations=[0, 1], patchlabel="0", facecolor="k", rotation=45
    )
    side(sankey, n=links_per_side)
    corner(sankey)
    side(sankey, n=links_per_side)
    corner(sankey)
    side(sankey, n=links_per_side)
    corner(sankey)
    side(sankey, n=links_per_side)
    sankey.finish()
    return matplotlib_to_svg(fig)
