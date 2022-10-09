"""
==========================
3D voxel / volumetric plot
==========================

Demonstrates plotting 3D volumetric objects with `.Axes3D.voxels`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/voxels.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import numpy as np


def app():
    (x, y, z) = np.indices((8, 8, 8))
    cube1 = ((x < 3) & (y < 3)) & (z < 3)
    cube2 = ((x >= 5) & (y >= 5)) & (z >= 5)
    link = ((abs((x - y)) + abs((y - z))) + abs((z - x))) <= 2
    voxelarray = (cube1 | cube2) | link
    colors = np.empty(voxelarray.shape, dtype=object)
    colors[link] = "red"
    colors[cube1] = "blue"
    colors[cube2] = "green"
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.voxels(voxelarray, facecolors=colors, edgecolor="k")
    return matplotlib_to_svg(fig)
