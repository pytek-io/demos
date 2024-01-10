"""
=================================
Triangular 3D filled contour plot
=================================

Filled contour plots of unstructured triangular grids.

The data used is the same as in the second plot of trisurf3d_demo2.
tricontour3d_demo shows the unfilled version of this example.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/tricontourf3d.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    n_angles = 48
    n_radii = 8
    min_radius = 0.25
    radii = np.linspace(min_radius, 0.95, n_radii)
    angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
    angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
    angles[:, 1::2] += np.pi / n_angles
    x = (radii * np.cos(angles)).flatten()
    y = (radii * np.sin(angles)).flatten()
    z = (np.cos(radii) * np.cos(3 * angles)).flatten()
    triang = tri.Triangulation(x, y)
    triang.set_mask(
        np.hypot(x[triang.triangles].mean(axis=1), y[triang.triangles].mean(axis=1))
        < min_radius
    )
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.tricontourf(triang, z, cmap=plt.cm.CMRmap)
    ax.view_init(elev=45.0)
    return matplotlib_to_svg(fig)
