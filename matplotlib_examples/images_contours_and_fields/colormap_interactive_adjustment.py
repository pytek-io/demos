"""
========================================
Interactive Adjustment of Colormap Range
========================================

Demonstration of how a colorbar can be used to interactively adjust the
range of colormapping on an image. To use the interactive feature, you must
be in either zoom mode (magnifying glass toolbar button) or
pan mode (4-way arrow toolbar button) and click inside the colorbar.

When zooming, the bounding box of the zoom region defines the new vmin and
vmax of the norm. Zooming using the right mouse button will expand the
vmin and vmax proportionally to the selected region, in the same manner that
one can zoom out on an axis. When panning, the vmin and vmax of the norm are
both shifted according to the direction of movement. The
Home/Back/Forward buttons can also be used to get back to a previous state.

.. redirect-from:: /gallery/userdemo/colormap_interactive_adjustment

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/colormap_interactive_adjustment.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import numpy as np


def app():
    t = np.linspace(0, (2 * np.pi), 1024)
    data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]
    (fig, ax) = plt.subplots()
    im = ax.imshow(data2d)
    ax.set_title(
        "Pan on the colorbar to shift the color mapping\nZoom on the colorbar to scale the color mapping"
    )
    fig.colorbar(im, ax=ax, label="Interactive colorbar")
    return matplotlib_to_svg(fig)
