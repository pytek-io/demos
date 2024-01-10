"""
=====================
Time Series Histogram
=====================

This example demonstrates how to efficiently visualize large numbers of time
series in a way that could potentially reveal hidden substructure and patterns
that are not immediately obvious, and display them in a visually appealing way.

In this example, we generate multiple sinusoidal "signal" series that are
buried under a larger number of random walk "noise/background" series. For an
unbiased Gaussian random walk with standard deviation of σ, the RMS deviation
from the origin after n steps is σ*sqrt(n). So in order to keep the sinusoids
visible on the same scale as the random walks, we scale the amplitude by the
random walk RMS. In addition, we also introduce a small random offset ``phi``
to shift the sines left/right, and some additive random noise to shift
individual data points up/down to make the signal a bit more "realistic" (you
wouldn't expect a perfect sine wave to appear in your data).

The first plot shows the typical way of visualizing multiple time series by
overlaying them on top of each other with ``plt.plot`` and a small value of
``alpha``. The second and third plots show how to reinterpret the data as a 2d
histogram, with optional interpolation between data points, by using
``np.histogram2d`` and ``plt.pcolormesh``.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/statistics/time_series_histogram.py.
"""
import matplotlib

matplotlib.use("Agg")
import time
from copy import copy

import matplotlib.pyplot as plt
import numpy as np
import numpy.matlib
from matplotlib.colors import LogNorm

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig, axes = plt.subplots(nrows=3, figsize=(6, 8), constrained_layout=True)
    num_series = 1000
    num_points = 100
    SNR = 0.1
    x = np.linspace(0, 4 * np.pi, num_points)
    Y = np.cumsum(np.random.randn(num_series, num_points), axis=-1)
    num_signal = int(round(SNR * num_series))
    phi = np.pi / 8 * np.random.randn(num_signal, 1)
    Y[-num_signal:] = np.sqrt(np.arange(num_points))[(None), :] * (
        np.sin(x[(None), :] - phi) + 0.05 * np.random.randn(num_signal, num_points)
    )
    tic = time.time()
    axes[0].plot(x, Y.T, color="C0", alpha=0.1)
    toc = time.time()
    axes[0].set_title("Line plot with alpha")
    print(f"{toc - tic:.3f} sec. elapsed")
    tic = time.time()
    num_fine = 800
    x_fine = np.linspace(x.min(), x.max(), num_fine)
    y_fine = np.empty((num_series, num_fine), dtype=float)
    for i in range(num_series):
        y_fine[(i), :] = np.interp(x_fine, x, Y[(i), :])
    y_fine = y_fine.flatten()
    x_fine = np.matlib.repmat(x_fine, num_series, 1).flatten()
    cmap = copy(plt.cm.plasma)
    cmap.set_bad(cmap(0))
    h, xedges, yedges = np.histogram2d(x_fine, y_fine, bins=[400, 100])
    pcm = axes[1].pcolormesh(
        xedges, yedges, h.T, cmap=cmap, norm=LogNorm(vmax=150.0), rasterized=True
    )
    fig.colorbar(pcm, ax=axes[1], label="# points", pad=0)
    axes[1].set_title("2d histogram and log color scale")
    pcm = axes[2].pcolormesh(
        xedges, yedges, h.T, cmap=cmap, vmax=150.0, rasterized=True
    )
    fig.colorbar(pcm, ax=axes[2], label="# points", pad=0)
    axes[2].set_title("2d histogram and linear color scale")
    toc = time.time()
    print(f"{toc - tic:.3f} sec. elapsed")
    return matplotlib_to_svg(fig)
