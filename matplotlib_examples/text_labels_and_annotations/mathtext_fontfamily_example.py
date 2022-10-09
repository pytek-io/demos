"""
===============
Math fontfamily
===============

A simple example showcasing the new *math_fontfamily* parameter that can
be used to change the family of fonts for each individual text
element in a plot.

If no parameter is set, the global value
:rc:`mathtext.fontset` will be used.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/text_labels_and_annotations/mathtext_fontfamily_example.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt


def app():
    (fig, ax) = plt.subplots(figsize=(6, 5))
    ax.plot(range(11), color="0.9")
    msg = "Normal Text. $Text\\ in\\ math\\ mode:\\ \\int_{0}^{\\infty } x^2 dx$"
    ax.text(1, 7, msg, size=12, math_fontfamily="cm")
    ax.text(1, 3, msg, size=12, math_fontfamily="dejavuserif")
    ax.set_title(
        "$Title\\ in\\ math\\ mode:\\ \\int_{0}^{\\infty } x^2 dx$",
        math_fontfamily="stixsans",
        size=14,
    )
    return matplotlib_to_svg(fig)
