"""
===============
Basic pie chart
===============

Demo of a basic pie chart plus a few additional features.

In addition to the basic pie chart, this demo shows a few optional features:

* slice labels
* auto-labeling the percentage
* offsetting a slice with "explode"
* drop-shadow
* custom start angle

Note about the custom start angle:

The default ``startangle`` is 0, which would start the "Frogs" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the frog slice starts on the
positive y-axis.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pie_and_polar_charts/pie_features.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def app(_):
    labels = "Frogs", "Hogs", "Dogs", "Logs"
    sizes = [15, 30, 45, 10]
    explode = 0, 0.1, 0, 0
    fig, ax1 = plt.subplots()
    ax1.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct="%1.1f%%",
        shadow=True,
        startangle=90,
    )
    ax1.axis("equal")
    return matplotlib_to_svg(fig)
