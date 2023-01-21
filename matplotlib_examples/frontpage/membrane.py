"""
======================
Frontpage plot example
======================

This example reproduces the frontpage simple plot example.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/frontpage/membrane.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.cbook as cbook
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    with cbook.get_sample_data("membrane.dat") as datafile:
        x = np.fromfile(datafile, np.float32)
    fig, ax = plt.subplots()
    ax.plot(x, linewidth=4)
    ax.set_xlim(5000, 6000)
    ax.set_ylim(-0.6, 0.1)
    ax.set_xticks([])
    ax.set_yticks([])
    fig.savefig("membrane_frontpage.png", dpi=25)
    return matplotlib_to_svg(fig)
