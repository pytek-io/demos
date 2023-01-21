"""
===========
Pcolor Demo
===========

Generating images with `~.axes.Axes.pcolor`.

Pcolor allows you to generate 2D image-style plots. Below we will show how
to do so in Matplotlib.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/pcolor_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

from demos.charts.utils import matplotlib_to_svg


def app():
    np.random.seed(19680801)
    Z = np.random.rand(6, 10)
    fig, (ax0, ax1) = plt.subplots(2, 1)
    c = ax0.pcolor(Z)
    ax0.set_title("default: no edges")
    c = ax1.pcolor(Z, edgecolors="k", linewidths=4)
    ax1.set_title("thick edges")
    fig.tight_layout()
    dx, dy = 0.15, 0.05
    y, x = np.mgrid[-3 : 3 + dy : dy, -3 : 3 + dx : dx]
    z = (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2) - y**2)
    z = z[:-1, :-1]
    z_min, z_max = -abs(z).max(), abs(z).max()
    fig, axs = plt.subplots(2, 2)
    ax = axs[0, 0]
    c = ax.pcolor(x, y, z, cmap="RdBu", vmin=z_min, vmax=z_max)
    ax.set_title("pcolor")
    fig.colorbar(c, ax=ax)
    ax = axs[0, 1]
    c = ax.pcolormesh(x, y, z, cmap="RdBu", vmin=z_min, vmax=z_max)
    ax.set_title("pcolormesh")
    fig.colorbar(c, ax=ax)
    ax = axs[1, 0]
    c = ax.imshow(
        z,
        cmap="RdBu",
        vmin=z_min,
        vmax=z_max,
        extent=[x.min(), x.max(), y.min(), y.max()],
        interpolation="nearest",
        origin="lower",
        aspect="auto",
    )
    ax.set_title('image (nearest, aspect="auto")')
    fig.colorbar(c, ax=ax)
    ax = axs[1, 1]
    c = ax.pcolorfast(x, y, z, cmap="RdBu", vmin=z_min, vmax=z_max)
    ax.set_title("pcolorfast")
    fig.colorbar(c, ax=ax)
    fig.tight_layout()
    N = 100
    X, Y = np.meshgrid(np.linspace(-3, 3, N), np.linspace(-2, 2, N))
    Z1 = np.exp(-(X**2) - Y**2)
    Z2 = np.exp(-((X * 10) ** 2) - (Y * 10) ** 2)
    Z = Z1 + 50 * Z2
    fig, (ax0, ax1) = plt.subplots(2, 1)
    c = ax0.pcolor(
        X, Y, Z, shading="auto", norm=LogNorm(vmin=Z.min(), vmax=Z.max()), cmap="PuBu_r"
    )
    fig.colorbar(c, ax=ax0)
    c = ax1.pcolor(X, Y, Z, cmap="PuBu_r", shading="auto")
    fig.colorbar(c, ax=ax1)
    return matplotlib_to_svg(fig)
