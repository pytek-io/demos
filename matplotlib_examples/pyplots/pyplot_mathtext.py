"""
===============
Pyplot Mathtext
===============

Use mathematical expressions in text labels. For an overview over MathText
see :doc:`/tutorials/text/mathtext`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/pyplot_mathtext.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def app():
    t = np.arange(0.0, 2.0, 0.01)
    s = np.sin(((2 * np.pi) * t))
    fig = plt.figure()
    plt.plot(t, s)
    plt.title("$\\alpha_i > \\beta_i$", fontsize=20)
    plt.text(1, (-0.6), "$\\sum_{i=0}^\\infty x_i$", fontsize=20)
    plt.text(0.6, 0.6, "$\\mathcal{A}\\mathrm{sin}(2 \\omega t)$", fontsize=20)
    plt.xlabel("time (s)")
    plt.ylabel("volts (mV)")
    return matplotlib_to_svg(fig)