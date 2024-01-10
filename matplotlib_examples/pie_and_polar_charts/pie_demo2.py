"""
=========
Pie Demo2
=========

Make a pie charts using `~.axes.Axes.pie`.

This example demonstrates some pie chart features like labels, varying size,
autolabeling the percentage, offsetting a slice and adding a shadow.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pie_and_polar_charts/pie_demo2.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def app(_):
    labels = "Frogs", "Hogs", "Dogs", "Logs"
    fracs = [15, 30, 45, 10]
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].pie(fracs, labels=labels, autopct="%1.1f%%", shadow=True)
    axs[0, 1].pie(
        fracs, labels=labels, autopct="%.0f%%", shadow=True, explode=(0, 0.1, 0, 0)
    )
    patches, texts, autotexts = axs[1, 0].pie(
        fracs,
        labels=labels,
        autopct="%.0f%%",
        textprops={"size": "smaller"},
        shadow=True,
        radius=0.5,
    )
    plt.setp(autotexts, size="x-small")
    autotexts[0].set_color("white")
    patches, texts, autotexts = axs[1, 1].pie(
        fracs,
        labels=labels,
        autopct="%.0f%%",
        textprops={"size": "smaller"},
        shadow=False,
        radius=0.5,
        explode=(0, 0.05, 0, 0),
    )
    plt.setp(autotexts, size="x-small")
    autotexts[0].set_color("white")
    return matplotlib_to_svg(fig)
