"""
=============
Unicode minus
=============

By default, tick labels at negative values are rendered using a `Unicode
minus`__ (U+2212) rather than an ASCII hyphen (U+002D).  This can be controlled
by setting :rc:`axes.unicode_minus`.

__ https://en.wikipedia.org/wiki/Plus_and_minus_signs#Character_codes

The replacement is performed at draw time of the tick labels (usually during a
`.pyplot.show()` or `.pyplot.savefig()` call). Therefore, all tick labels of
the figure follow the same setting and we cannot demonstrate both glyphs on
real tick labels of the same figure simultaneously.

Instead, this example simply showcases the difference between the two glyphs
in a magnified font.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/text_labels_and_annotations/unicode_minus.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt


def app():
    fig = plt.figure(figsize=(4, 2))
    fig.text(0.15, 0.6, "Unicode minus:", fontsize=20)
    fig.text(0.85, 0.6, "−1", ha="right", fontsize=20)
    fig.text(0.15, 0.3, "ASCII hyphen:", fontsize=20)
    fig.text(0.85, 0.3, "-1", ha="right", fontsize=20)
    return matplotlib_to_svg(fig)
