"""
===========================
Rotating custom tick labels
===========================

Demo of custom tick-labels with user-defined rotation.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/ticks/ticklabels_rotation.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def app():
    x = [1, 2, 3, 4]
    y = [1, 4, 9, 6]
    labels = ["Frogs", "Hogs", "Bogs", "Slogs"]
    fig = plt.figure()
    plt.plot(x, y)
    plt.xticks(x, labels, rotation="vertical")
    plt.margins(0.2)
    plt.subplots_adjust(bottom=0.15)
    return matplotlib_to_svg(fig)
