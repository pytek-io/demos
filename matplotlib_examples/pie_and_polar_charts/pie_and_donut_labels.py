"""
==========================
Labeling a pie and a donut
==========================

Welcome to the Matplotlib bakery. We will create a pie and a donut
chart through the `pie method <matplotlib.axes.Axes.pie>` and
show how to label them with a `legend <matplotlib.axes.Axes.legend>`
as well as with `annotations <matplotlib.axes.Axes.annotate>`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pie_and_polar_charts/pie_and_donut_labels.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def func(pct, allvals):
    absolute = int(np.round(((pct / 100.0) * np.sum(allvals))))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)


def app():
    recipe = ["375 g flour", "75 g sugar", "250 g butter", "300 g berries"]
    data = [float(x.split()[0]) for x in recipe]
    ingredients = [x.split()[(-1)] for x in recipe]
    (fig, ax) = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    (wedges, texts, autotexts) = ax.pie(
        data, autopct=(lambda pct: func(pct, data)), textprops=dict(color="w")
    )
    ax.legend(
        wedges,
        ingredients,
        title="Ingredients",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
    )
    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title("Matplotlib bakery: A pie")
    (fig, ax) = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    recipe = [
        "225 g flour",
        "90 g sugar",
        "1 egg",
        "60 g butter",
        "100 ml milk",
        "1/2 package of yeast",
    ]
    data = [225, 90, 50, 60, 100, 5]
    (wedges, texts) = ax.pie(data, wedgeprops=dict(width=0.5), startangle=(-40))
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")
    for (i, p) in enumerate(wedges):
        ang = ((p.theta2 - p.theta1) / 2.0) + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {(-1): "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(
            recipe[i],
            xy=(x, y),
            xytext=((1.35 * np.sign(x)), (1.4 * y)),
            horizontalalignment=horizontalalignment,
            **kw
        )
    ax.set_title("Matplotlib bakery: A donut")
    return matplotlib_to_svg(fig)
