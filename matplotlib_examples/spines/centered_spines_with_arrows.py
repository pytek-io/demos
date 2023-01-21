"""
===========================
Centered spines with arrows
===========================

This example shows a way to draw a "math textbook" style plot, where the
spines ("axes lines") are drawn at ``x = 0`` and ``y = 0``, and have arrows at
their ends.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/spines/centered_spines_with_arrows.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    fig, ax = plt.subplots()
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    x = np.linspace(-0.5, 1.0, 100)
    ax.plot(x, np.sin(x * np.pi))
    return matplotlib_to_svg(fig)
