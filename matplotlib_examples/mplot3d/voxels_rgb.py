"""
==========================================
3D voxel / volumetric plot with rgb colors
==========================================

Demonstrates using `.Axes3D.voxels` to visualize parts of a color space.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/voxels_rgb.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x


def app():
    r, g, b = np.indices((17, 17, 17)) / 16.0
    rc = midpoints(r)
    gc = midpoints(g)
    bc = midpoints(b)
    sphere = (rc - 0.5) ** 2 + (gc - 0.5) ** 2 + (bc - 0.5) ** 2 < 0.5**2
    colors = np.zeros(sphere.shape + (3,))
    colors[..., 0] = rc
    colors[..., 1] = gc
    colors[..., 2] = bc
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.voxels(
        r,
        g,
        b,
        sphere,
        facecolors=colors,
        edgecolors=np.clip(2 * colors - 0.5, 0, 1),
        linewidth=0.5,
    )
    ax.set(xlabel="r", ylabel="g", zlabel="b")
    return matplotlib_to_svg(fig)
