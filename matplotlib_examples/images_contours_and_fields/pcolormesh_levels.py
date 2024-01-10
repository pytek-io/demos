"""
==========
pcolormesh
==========

`.axes.Axes.pcolormesh` allows you to generate 2D image-style plots.  Note it
is faster than the similar `~.axes.Axes.pcolor`.


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/pcolormesh_levels.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

from demos.charts.utils import matplotlib_to_svg


def app(_):
    np.random.seed(19680801)
    Z = np.random.rand(6, 10)
    x = np.arange(-0.5, 10, 1)
    y = np.arange(4.5, 11, 1)
    fig, ax = plt.subplots()
    ax.pcolormesh(x, y, Z)
    x = np.arange(-0.5, 10, 1)
    y = np.arange(4.5, 11, 1)
    X, Y = np.meshgrid(x, y)
    X = X + 0.2 * Y
    Y = Y + 0.3 * X
    fig, ax = plt.subplots()
    ax.pcolormesh(X, Y, Z)
    x = np.arange(10)
    y = np.arange(6)
    X, Y = np.meshgrid(x, y)
    fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
    axs[0].pcolormesh(X, Y, Z, vmin=np.min(Z), vmax=np.max(Z), shading="auto")
    axs[0].set_title("shading='auto' = 'nearest'")
    axs[1].pcolormesh(X, Y, Z[:-1, :-1], vmin=np.min(Z), vmax=np.max(Z), shading="flat")
    axs[1].set_title("shading='flat'")
    dx, dy = 0.05, 0.05
    y, x = np.mgrid[slice(1, 5 + dy, dy), slice(1, 5 + dx, dx)]
    z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
    z = z[:-1, :-1]
    levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())
    cmap = plt.colormaps["PiYG"]
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    fig, (ax0, ax1) = plt.subplots(nrows=2)
    im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
    fig.colorbar(im, ax=ax0)
    ax0.set_title("pcolormesh with levels")
    cf = ax1.contourf(
        x[:-1, :-1] + dx / 2.0, y[:-1, :-1] + dy / 2.0, z, levels=levels, cmap=cmap
    )
    fig.colorbar(cf, ax=ax1)
    ax1.set_title("contourf with levels")
    fig.tight_layout()
    return matplotlib_to_svg(fig)
