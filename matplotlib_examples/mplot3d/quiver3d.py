"""
==============
3D quiver plot
==============

Demonstrates plotting directional arrows at points on a 3D meshgrid.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/quiver3d.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    x, y, z = np.meshgrid(
        np.arange(-0.8, 1, 0.2), np.arange(-0.8, 1, 0.2), np.arange(-0.8, 1, 0.8)
    )
    u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
    v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
    w = np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) * np.sin(np.pi * z)
    ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
    return matplotlib_to_svg(fig)
