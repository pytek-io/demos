"""
=================
Nested pie charts
=================

The following examples show two ways to build a nested pie chart
in Matplotlib. Such charts are often referred to as donut charts.


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pie_and_polar_charts/nested_pie.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import numpy as np


def app():
    (fig, ax) = plt.subplots()
    size = 0.3
    vals = np.array([[60.0, 32.0], [37.0, 40.0], [29.0, 10.0]])
    cmap = plt.colormaps["tab20c"]
    outer_colors = cmap((np.arange(3) * 4))
    inner_colors = cmap([1, 2, 5, 6, 9, 10])
    ax.pie(
        vals.sum(axis=1),
        radius=1,
        colors=outer_colors,
        wedgeprops=dict(width=size, edgecolor="w"),
    )
    ax.pie(
        vals.flatten(),
        radius=(1 - size),
        colors=inner_colors,
        wedgeprops=dict(width=size, edgecolor="w"),
    )
    ax.set(aspect="equal", title="Pie plot with `ax.pie`")
    (fig, ax) = plt.subplots(subplot_kw=dict(projection="polar"))
    size = 0.3
    vals = np.array([[60.0, 32.0], [37.0, 40.0], [29.0, 10.0]])
    valsnorm = ((vals / np.sum(vals)) * 2) * np.pi
    valsleft = np.cumsum(np.append(0, valsnorm.flatten()[:(-1)])).reshape(vals.shape)
    cmap = plt.colormaps["tab20c"]
    outer_colors = cmap((np.arange(3) * 4))
    inner_colors = cmap([1, 2, 5, 6, 9, 10])
    ax.bar(
        x=valsleft[:, 0],
        width=valsnorm.sum(axis=1),
        bottom=(1 - size),
        height=size,
        color=outer_colors,
        edgecolor="w",
        linewidth=1,
        align="edge",
    )
    ax.bar(
        x=valsleft.flatten(),
        width=valsnorm.flatten(),
        bottom=(1 - (2 * size)),
        height=size,
        color=inner_colors,
        edgecolor="w",
        linewidth=1,
        align="edge",
    )
    ax.set(title="Pie plot with `ax.bar` and polar coordinates")
    ax.set_axis_off()
    return matplotlib_to_svg(fig)
