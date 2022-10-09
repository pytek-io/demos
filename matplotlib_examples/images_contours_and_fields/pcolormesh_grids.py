"""
============================
pcolormesh grids and shading
============================

`.axes.Axes.pcolormesh` and `~.axes.Axes.pcolor` have a few options for
how grids are laid out and the shading between the grid points.

Generally, if *Z* has shape *(M, N)* then the grid *X* and *Y* can be
specified with either shape *(M+1, N+1)* or *(M, N)*, depending on the
argument for the ``shading`` keyword argument.  Note that below we specify
vectors *x* as either length N or N+1 and *y* as length M or M+1, and
`~.axes.Axes.pcolormesh` internally makes the mesh matrices *X* and *Y* from
the input vectors.


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/pcolormesh_grids.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.pyplot as plt
import numpy as np


def _annotate(ax, x, y, title):
    (X, Y) = np.meshgrid(x, y)
    ax.plot(X.flat, Y.flat, "o", color="m")
    ax.set_xlim((-0.7), 5.2)
    ax.set_ylim((-0.7), 3.2)
    ax.set_title(title)


def app():
    nrows = 3
    ncols = 5
    Z = np.arange((nrows * ncols)).reshape(nrows, ncols)
    x = np.arange((ncols + 1))
    y = np.arange((nrows + 1))
    (fig, ax) = plt.subplots()
    ax.pcolormesh(x, y, Z, shading="flat", vmin=Z.min(), vmax=Z.max())
    _annotate(ax, x, y, "shading='flat'")
    x = np.arange(ncols)
    y = np.arange(nrows)
    (fig, ax) = plt.subplots()
    ax.pcolormesh(x, y, Z[:(-1), :(-1)], shading="flat", vmin=Z.min(), vmax=Z.max())
    _annotate(ax, x, y, "shading='flat': X, Y, C same shape")
    (fig, ax) = plt.subplots()
    ax.pcolormesh(x, y, Z, shading="nearest", vmin=Z.min(), vmax=Z.max())
    _annotate(ax, x, y, "shading='nearest'")
    (fig, axs) = plt.subplots(2, 1, constrained_layout=True)
    ax = axs[0]
    x = np.arange(ncols)
    y = np.arange(nrows)
    ax.pcolormesh(x, y, Z, shading="auto", vmin=Z.min(), vmax=Z.max())
    _annotate(ax, x, y, "shading='auto'; X, Y, Z: same shape (nearest)")
    ax = axs[1]
    x = np.arange((ncols + 1))
    y = np.arange((nrows + 1))
    ax.pcolormesh(x, y, Z, shading="auto", vmin=Z.min(), vmax=Z.max())
    _annotate(ax, x, y, "shading='auto'; X, Y one larger than Z (flat)")
    (fig, ax) = plt.subplots(constrained_layout=True)
    x = np.arange(ncols)
    y = np.arange(nrows)
    ax.pcolormesh(x, y, Z, shading="gouraud", vmin=Z.min(), vmax=Z.max())
    _annotate(ax, x, y, "shading='gouraud'; X, Y same shape as Z")
    return matplotlib_to_svg(fig)
