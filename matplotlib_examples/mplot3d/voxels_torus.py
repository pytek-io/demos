"""
=======================================================
3D voxel / volumetric plot with cylindrical coordinates
=======================================================

Demonstrates using the *x*, *y*, *z* parameters of `.Axes3D.voxels`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/voxels_torus.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.colors
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
    r, theta, z = np.mgrid[0:1:11.0j, 0 : np.pi * 2 : 25.0j, -0.5:0.5:11.0j]
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    rc, thetac, zc = midpoints(r), midpoints(theta), midpoints(z)
    sphere = (rc - 0.7) ** 2 + (zc + 0.2 * np.cos(thetac * 2)) ** 2 < 0.2**2
    hsv = np.zeros(sphere.shape + (3,))
    hsv[..., 0] = thetac / (np.pi * 2)
    hsv[..., 1] = rc
    hsv[..., 2] = zc + 0.5
    colors = matplotlib.colors.hsv_to_rgb(hsv)
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.voxels(
        x,
        y,
        z,
        sphere,
        facecolors=colors,
        edgecolors=np.clip(2 * colors - 0.5, 0, 1),
        linewidth=0.5,
    )
    return matplotlib_to_svg(fig)
