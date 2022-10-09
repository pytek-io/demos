"""
====================
Frontpage 3D example
====================

This example reproduces the frontpage 3D example.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/frontpage/3D.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource
import matplotlib.pyplot as plt
import numpy as np


def app():
    dem = cbook.get_sample_data("jacksboro_fault_dem.npz", np_load=True)
    z = dem["elevation"]
    (nrows, ncols) = z.shape
    x = np.linspace(dem["xmin"], dem["xmax"], ncols)
    y = np.linspace(dem["ymin"], dem["ymax"], nrows)
    (x, y) = np.meshgrid(x, y)
    region = np.s_[5:50, 5:50]
    (x, y, z) = (x[region], y[region], z[region])
    (fig, ax) = plt.subplots(subplot_kw=dict(projection="3d"))
    ls = LightSource(270, 45)
    rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode="soft")
    surf = ax.plot_surface(
        x,
        y,
        z,
        rstride=1,
        cstride=1,
        facecolors=rgb,
        linewidth=0,
        antialiased=False,
        shade=False,
    )
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    fig.savefig("surface3d_frontpage.png", dpi=25)
    return matplotlib_to_svg(fig)
