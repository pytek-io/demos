"""
==========
Bar of pie
==========

Make a "bar of pie" chart where the first slice of the pie is
"exploded" into a bar chart with a further breakdown of said slice's
characteristics. The example demonstrates using a figure with multiple
sets of axes and using the axes patches list to add two ConnectionPatches
to link the subplot charts.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pie_and_polar_charts/bar_of_pie.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np


def app():
    (fig, (ax1, ax2)) = plt.subplots(1, 2, figsize=(9, 5))
    fig.subplots_adjust(wspace=0)
    overall_ratios = [0.27, 0.56, 0.17]
    labels = ["Approve", "Disapprove", "Undecided"]
    explode = [0.1, 0, 0]
    angle = (-180) * overall_ratios[0]
    (wedges, *_) = ax1.pie(
        overall_ratios,
        autopct="%1.1f%%",
        startangle=angle,
        labels=labels,
        explode=explode,
    )
    age_ratios = [0.33, 0.54, 0.07, 0.06]
    age_labels = ["Under 35", "35-49", "50-65", "Over 65"]
    bottom = 1
    width = 0.2
    for (j, (height, label)) in enumerate(reversed([*zip(age_ratios, age_labels)])):
        bottom -= height
        bc = ax2.bar(
            0,
            height,
            width,
            bottom=bottom,
            color="C0",
            label=label,
            alpha=(0.1 + (0.25 * j)),
        )
        ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type="center")
    ax2.set_title("Age of approvers")
    ax2.legend()
    ax2.axis("off")
    ax2.set_xlim(((-2.5) * width), (2.5 * width))
    (theta1, theta2) = (wedges[0].theta1, wedges[0].theta2)
    (center, r) = (wedges[0].center, wedges[0].r)
    bar_height = sum(age_ratios)
    x = (r * np.cos(((np.pi / 180) * theta2))) + center[0]
    y = (r * np.sin(((np.pi / 180) * theta2))) + center[1]
    con = ConnectionPatch(
        xyA=(((-width) / 2), bar_height),
        coordsA=ax2.transData,
        xyB=(x, y),
        coordsB=ax1.transData,
    )
    con.set_color([0, 0, 0])
    con.set_linewidth(4)
    ax2.add_artist(con)
    x = (r * np.cos(((np.pi / 180) * theta1))) + center[0]
    y = (r * np.sin(((np.pi / 180) * theta1))) + center[1]
    con = ConnectionPatch(
        xyA=(((-width) / 2), 0),
        coordsA=ax2.transData,
        xyB=(x, y),
        coordsB=ax1.transData,
    )
    con.set_color([0, 0, 0])
    ax2.add_artist(con)
    con.set_linewidth(4)
    return matplotlib_to_svg(fig)
