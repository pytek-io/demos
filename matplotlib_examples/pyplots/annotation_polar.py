"""
================
Annotation Polar
================

This example shows how to create an annotation on a polar graph.

For a complete overview of the annotation capabilities, also see the
:doc:`annotation tutorial</tutorials/text/annotations>`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/annotation_polar.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    fig = plt.figure()
    ax = fig.add_subplot(projection="polar")
    r = np.arange(0, 1, 0.001)
    theta = 2 * 2 * np.pi * r
    (line,) = ax.plot(theta, r, color="#ee8d18", lw=3)
    ind = 800
    thisr, thistheta = r[ind], theta[ind]
    ax.plot([thistheta], [thisr], "o")
    ax.annotate(
        "a polar annotation",
        xy=(thistheta, thisr),
        xytext=(0.05, 0.05),
        textcoords="figure fraction",
        arrowprops={"facecolor": "black", "shrink": 0.05},
        horizontalalignment="left",
        verticalalignment="bottom",
    )
    return matplotlib_to_svg(fig)
