"""
Placing text boxes
==================

When decorating axes with text boxes, two useful tricks are to place the text
in axes coordinates (see :doc:`/tutorials/advanced/transforms_tutorial`),
so the text doesn't move around with changes in x or y limits.  You
can also use the ``bbox`` property of text to surround the text with a
`~matplotlib.patches.Patch` instance -- the ``bbox`` keyword argument takes a
dictionary with keys that are Patch properties.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/text_labels_and_annotations/placing_text_boxes.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    np.random.seed(19680801)
    fig, ax = plt.subplots()
    x = 30 * np.random.randn(10000)
    mu = x.mean()
    median = np.median(x)
    sigma = x.std()
    textstr = "\n".join(
        (
            "$\\mu=%.2f$" % (mu,),
            "$\\mathrm{median}=%.2f$" % (median,),
            "$\\sigma=%.2f$" % (sigma,),
        )
    )
    ax.hist(x, 50)
    props = {"boxstyle": "round", "facecolor": "wheat", "alpha": 0.5}
    ax.text(
        0.05,
        0.95,
        textstr,
        transform=ax.transAxes,
        fontsize=14,
        verticalalignment="top",
        bbox=props,
    )
    return matplotlib_to_svg(fig)
