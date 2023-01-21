"""
===============================
3D voxel plot of the numpy logo
===============================

Demonstrates using `.Axes3D.voxels` with uneven coordinates.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/voxels_numpy_logo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def explode(data):
    size = np.array(data.shape) * 2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e


def app():
    n_voxels = np.zeros((4, 3, 4), dtype=bool)
    n_voxels[(0), (0), :] = True
    n_voxels[(-1), (0), :] = True
    n_voxels[1, 0, 2] = True
    n_voxels[2, 0, 1] = True
    facecolors = np.where(n_voxels, "#FFD65DC0", "#7A88CCC0")
    edgecolors = np.where(n_voxels, "#BFAB6E", "#7D84A6")
    filled = np.ones(n_voxels.shape)
    filled_2 = explode(filled)
    fcolors_2 = explode(facecolors)
    ecolors_2 = explode(edgecolors)
    x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float) // 2
    x[0::2, :, :] += 0.05
    y[:, 0::2, :] += 0.05
    z[:, :, 0::2] += 0.05
    x[1::2, :, :] += 0.95
    y[:, 1::2, :] += 0.95
    z[:, :, 1::2] += 0.95
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)
    return matplotlib_to_svg(fig)
