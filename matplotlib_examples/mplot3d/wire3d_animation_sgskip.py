"""
=============================
Animating a 3D wireframe plot
=============================

A very simple 'animation' of a 3D plot.  See also rotate_axes3d_demo.

(This example is skipped when building the documentation gallery because it
intentionally takes a long time to run)

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/wire3d_animation_sgskip.py.
"""
import matplotlib

matplotlib.use("Agg")
import time

import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def generate(X, Y, phi):
    """
    Generates Z data for the points in the X, Y meshgrid and parameter phi.
    """
    R = 1 - np.sqrt(X**2 + Y**2)
    return np.cos(2 * np.pi * X + phi) * R


def app():
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    xs = np.linspace(-1, 1, 50)
    ys = np.linspace(-1, 1, 50)
    X, Y = np.meshgrid(xs, ys)
    ax.set_zlim(-1, 1)
    wframe = None
    tstart = time.time()
    for phi in np.linspace(0, 180.0 / np.pi, 100):
        if wframe:
            wframe.remove()
        Z = generate(X, Y, phi)
        wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
        plt.pause(0.001)
    print("Average FPS: %f" % (100 / (time.time() - tstart)))
    return matplotlib_to_svg(fig)
