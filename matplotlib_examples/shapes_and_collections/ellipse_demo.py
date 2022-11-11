"""
============
Ellipse Demo
============

Draw many ellipses. Here individual ellipses are drawn. Compare this
to the :doc:`Ellipse collection example
</gallery/shapes_and_collections/ellipse_collection>`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/shapes_and_collections/ellipse_demo.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse


def app():
    np.random.seed(19680801)
    NUM = 250
    ells = [
        Ellipse(
            xy=(np.random.rand(2) * 10),
            width=np.random.rand(),
            height=np.random.rand(),
            angle=(np.random.rand() * 360),
        )
        for i in range(NUM)
    ]
    (fig, ax) = plt.subplots(subplot_kw={"aspect": "equal"})
    for e in ells:
        ax.add_artist(e)
        e.set_clip_box(ax.bbox)
        e.set_alpha(np.random.rand())
        e.set_facecolor(np.random.rand(3))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    angle_step = 45
    angles = np.arange(0, 180, angle_step)
    (fig, ax) = plt.subplots(subplot_kw={"aspect": "equal"})
    for angle in angles:
        ellipse = Ellipse((0, 0), 4, 2, angle=angle, alpha=0.1)
        ax.add_artist(ellipse)
    ax.set_xlim((-2.2), 2.2)
    ax.set_ylim((-2.2), 2.2)
    return matplotlib_to_svg(fig)