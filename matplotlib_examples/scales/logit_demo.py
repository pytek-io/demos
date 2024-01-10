"""
================
Logit Demo
================

Examples of plots with logit axes.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/scales/logit_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import math

import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    xmax = 10
    x = np.linspace(-xmax, xmax, 10000)
    cdf_norm = [(math.erf(w / np.sqrt(2)) / 2 + 1 / 2) for w in x]
    cdf_laplacian = np.where(x < 0, 1 / 2 * np.exp(x), 1 - 1 / 2 * np.exp(-x))
    cdf_cauchy = np.arctan(x) / np.pi + 1 / 2
    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(6.4, 8.5))
    for i in range(3):
        for j in range(2):
            axs[i, j].plot(x, cdf_norm, label="$\\mathcal{N}$")
            axs[i, j].plot(x, cdf_laplacian, label="$\\mathcal{L}$")
            axs[i, j].plot(x, cdf_cauchy, label="Cauchy")
            axs[i, j].legend()
            axs[i, j].grid()
    axs[0, 0].set(title="logit scale")
    axs[0, 0].set_yscale("logit")
    axs[0, 0].set_ylim(1e-05, 1 - 1e-05)
    axs[0, 1].set(title="logit scale")
    axs[0, 1].set_yscale("logit")
    axs[0, 1].set_xlim(0, xmax)
    axs[0, 1].set_ylim(0.8, 1 - 0.005)
    axs[1, 0].set(title="logit scale")
    axs[1, 0].set_yscale("logit", one_half="1/2", use_overline=True)
    axs[1, 0].set_ylim(1e-05, 1 - 1e-05)
    axs[1, 1].set(title="logit scale")
    axs[1, 1].set_yscale("logit", one_half="1/2", use_overline=True)
    axs[1, 1].set_xlim(0, xmax)
    axs[1, 1].set_ylim(0.8, 1 - 0.005)
    axs[2, 0].set(title="linear scale")
    axs[2, 0].set_ylim(0, 1)
    axs[2, 1].set(title="linear scale")
    axs[2, 1].set_xlim(0, xmax)
    axs[2, 1].set_ylim(0.8, 1)
    fig.tight_layout()
    return matplotlib_to_svg(fig)
