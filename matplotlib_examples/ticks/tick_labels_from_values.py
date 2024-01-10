"""
=========================================
Setting tick labels from a list of values
=========================================

Using `.Axes.set_xticks` causes the tick labels to be set on the currently
chosen ticks. However, you may want to allow matplotlib to dynamically
choose the number of ticks and their spacing.

In this case it may be better to determine the tick label from the
value at the tick. The following example shows how to do this.

NB: The `.ticker.MaxNLocator` is used here to ensure that the tick values
take integer values.


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/ticks/tick_labels_from_values.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from demos.charts.utils import matplotlib_to_svg

fig, ax = plt.subplots()
xs = range(26)
ys = range(26)
labels = list("abcdefghijklmnopqrstuvwxyz")


def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ""


def app(_):
    ax.xaxis.set_major_formatter(format_fn)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.plot(xs, ys)
    return matplotlib_to_svg(fig)
