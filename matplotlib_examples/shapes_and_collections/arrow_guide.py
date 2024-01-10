"""
===========
Arrow guide
===========

Adding arrow patches to plots.

Arrows are often used to annotate plots. This tutorial shows how to plot arrows
that behave differently when the data limits on a plot are changed. In general,
points on a plot can either be fixed in "data space" or "display space".
Something plotted in data space moves when the data limits are altered - an
example would be the points in a scatter plot. Something plotted in display
space stays static when data limits are altered - an example would be a
figure title or the axis labels.

Arrows consist of a head (and possibly a tail) and a stem drawn between a
start point and end point, called 'anchor points' from now on.
Here we show three use cases for plotting arrows, depending on whether the
head or anchor points need to be fixed in data or display space:

1. Head shape fixed in display space, anchor points fixed in data space
2. Head shape and anchor points fixed in display space
3. Entire patch fixed in data space

Below each use case is presented in turn.

.. redirect-from:: /gallery/text_labels_and_annotations/arrow_simple_demo

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/shapes_and_collections/arrow_guide.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def app(_):
    x_tail = 0.1
    y_tail = 0.5
    x_head = 0.9
    y_head = 0.8
    dx = x_head - x_tail
    dy = y_head - y_tail
    fig, axs = plt.subplots(nrows=2)
    arrow = mpatches.FancyArrowPatch(
        (x_tail, y_tail), (x_head, y_head), mutation_scale=100
    )
    axs[0].add_patch(arrow)
    arrow = mpatches.FancyArrowPatch(
        (x_tail, y_tail), (x_head, y_head), mutation_scale=100
    )
    axs[1].add_patch(arrow)
    axs[1].set(xlim=(0, 2), ylim=(0, 2))
    fig, axs = plt.subplots(nrows=2)
    arrow = mpatches.FancyArrowPatch(
        (x_tail, y_tail),
        (x_head, y_head),
        mutation_scale=100,
        transform=axs[0].transAxes,
    )
    axs[0].add_patch(arrow)
    arrow = mpatches.FancyArrowPatch(
        (x_tail, y_tail),
        (x_head, y_head),
        mutation_scale=100,
        transform=axs[1].transAxes,
    )
    axs[1].add_patch(arrow)
    axs[1].set(xlim=(0, 2), ylim=(0, 2))
    fig, axs = plt.subplots(nrows=2)
    arrow = mpatches.Arrow(x_tail, y_tail, dx, dy)
    axs[0].add_patch(arrow)
    arrow = mpatches.FancyArrow(
        x_tail, y_tail - 0.4, dx, dy, width=0.1, length_includes_head=True, color="C1"
    )
    axs[0].add_patch(arrow)
    axs[0].arrow(
        x_tail + 1,
        y_tail - 0.4,
        dx,
        dy,
        width=0.1,
        length_includes_head=True,
        color="C2",
    )
    arrow = mpatches.Arrow(x_tail, y_tail, dx, dy)
    axs[1].add_patch(arrow)
    arrow = mpatches.FancyArrow(
        x_tail, y_tail - 0.4, dx, dy, width=0.1, length_includes_head=True, color="C1"
    )
    axs[1].add_patch(arrow)
    axs[1].arrow(
        x_tail + 1,
        y_tail - 0.4,
        dx,
        dy,
        width=0.1,
        length_includes_head=True,
        color="C2",
    )
    axs[1].set(xlim=(0, 2), ylim=(0, 2))
    return matplotlib_to_svg(fig)
