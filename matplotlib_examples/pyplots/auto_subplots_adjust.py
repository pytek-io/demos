"""
===============================================
Programmatically controlling subplot adjustment
===============================================

.. note::

    This example is primarily intended to show some advanced concepts in
    Matplotlib.

    If you are only looking for having enough space for your labels, it is
    almost always simpler and good enough to either set the subplot parameters
    manually using `.Figure.subplots_adjust`, or use one of the automatic
    layout mechanisms
    (:doc:`/tutorials/intermediate/constrainedlayout_guide` or
    :doc:`/tutorials/intermediate/tight_layout_guide`).

This example describes a user-defined way to read out Artist sizes and
set the subplot parameters accordingly. Its main purpose is to illustrate
some advanced concepts like reading out text positions, working with
bounding boxes and transforms and using
:ref:`events <event-handling-tutorial>`. But it can also serve as a starting
point if you want to automate the layouting and need more flexibility than
tight layout and constrained layout.

Below, we collect the bounding boxes of all y-labels and move the left border
of the subplot to the right so that it leaves enough room for the union of all
the bounding boxes.

There's one catch with calculating text bounding boxes:
Querying the text bounding boxes (`.Text.get_window_extent`) needs a
renderer (`.RendererBase` instance), to calculate the text size. This renderer
is only available after the figure has been drawn (`.Figure.draw`).

A solution to this is putting the adjustment logic in a draw callback.
This function is executed after the figure has been drawn. It can now check
if the subplot leaves enough room for the text. If not, the subplot parameters
are updated and second draw is triggered.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/auto_subplots_adjust.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms

(fig, ax) = plt.subplots()
ax.plot(range(10))
ax.set_yticks([2, 5, 7], labels=["really, really, really", "long", "labels"])


def on_draw(event):
    bboxes = []
    for label in ax.get_yticklabels():
        bbox_px = label.get_window_extent()
        bbox_fig = bbox_px.transformed(fig.transFigure.inverted())
        bboxes.append(bbox_fig)
    bbox = mtransforms.Bbox.union(bboxes)
    if fig.subplotpars.left < bbox.width:
        fig.subplots_adjust(left=(1.1 * bbox.width))
        fig.canvas.draw()


def app():
    fig.canvas.mpl_connect("draw_event", on_draw)
    return matplotlib_to_svg(fig)
