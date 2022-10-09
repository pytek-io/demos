"""
==================
Colormap reference
==================

Reference for colormaps included with Matplotlib.

A reversed version of each of these colormaps is available by appending
``_r`` to the name, e.g., ``viridis_r``.

See :doc:`/tutorials/colors/colormaps` for an in-depth discussion about
colormaps, including colorblind-friendliness.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/color/colormap_reference.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt

cmaps = [
    (
        "Perceptually Uniform Sequential",
        ["viridis", "plasma", "inferno", "magma", "cividis"],
    ),
    (
        "Sequential",
        [
            "Greys",
            "Purples",
            "Blues",
            "Greens",
            "Oranges",
            "Reds",
            "YlOrBr",
            "YlOrRd",
            "OrRd",
            "PuRd",
            "RdPu",
            "BuPu",
            "GnBu",
            "PuBu",
            "YlGnBu",
            "PuBuGn",
            "BuGn",
            "YlGn",
        ],
    ),
    (
        "Sequential (2)",
        [
            "binary",
            "gist_yarg",
            "gist_gray",
            "gray",
            "bone",
            "pink",
            "spring",
            "summer",
            "autumn",
            "winter",
            "cool",
            "Wistia",
            "hot",
            "afmhot",
            "gist_heat",
            "copper",
        ],
    ),
    (
        "Diverging",
        [
            "PiYG",
            "PRGn",
            "BrBG",
            "PuOr",
            "RdGy",
            "RdBu",
            "RdYlBu",
            "RdYlGn",
            "Spectral",
            "coolwarm",
            "bwr",
            "seismic",
        ],
    ),
    ("Cyclic", ["twilight", "twilight_shifted", "hsv"]),
    (
        "Qualitative",
        [
            "Pastel1",
            "Pastel2",
            "Paired",
            "Accent",
            "Dark2",
            "Set1",
            "Set2",
            "Set3",
            "tab10",
            "tab20",
            "tab20b",
            "tab20c",
        ],
    ),
    (
        "Miscellaneous",
        [
            "flag",
            "prism",
            "ocean",
            "gist_earth",
            "terrain",
            "gist_stern",
            "gnuplot",
            "gnuplot2",
            "CMRmap",
            "cubehelix",
            "brg",
            "gist_rainbow",
            "rainbow",
            "jet",
            "turbo",
            "nipy_spectral",
            "gist_ncar",
        ],
    ),
]
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(cmap_category, cmap_list):
    nrows = len(cmap_list)
    figh = (0.35 + 0.15) + ((nrows + ((nrows - 1) * 0.1)) * 0.22)
    (fig, axs) = plt.subplots(nrows=nrows, figsize=(6.4, figh))
    fig.subplots_adjust(
        top=(1 - (0.35 / figh)), bottom=(0.15 / figh), left=0.2, right=0.99
    )
    axs[0].set_title((cmap_category + " colormaps"), fontsize=14)
    for (ax, cmap_name) in zip(axs, cmap_list):
        ax.imshow(gradient, aspect="auto", cmap=cmap_name)
        ax.text(
            (-0.01),
            0.5,
            cmap_name,
            va="center",
            ha="right",
            fontsize=10,
            transform=ax.transAxes,
        )
    for ax in axs:
        ax.set_axis_off()
    return fig


def app():
    for (cmap_category, cmap_list) in cmaps:
        fig = plot_color_gradients(cmap_category, cmap_list)
        break
    return matplotlib_to_svg(fig)
