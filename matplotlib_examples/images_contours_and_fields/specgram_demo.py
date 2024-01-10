"""
================
Spectrogram Demo
================

Demo of a spectrogram plot (`~.axes.Axes.specgram`).

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/specgram_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    np.random.seed(19680801)
    dt = 0.0005
    t = np.arange(0.0, 20.0, dt)
    s1 = np.sin(2 * np.pi * 100 * t)
    s2 = 2 * np.sin(2 * np.pi * 400 * t)
    s2[t <= 10] = s2[12 <= t] = 0
    nse = 0.01 * np.random.random(size=len(t))
    x = s1 + s2 + nse
    NFFT = 1024
    Fs = int(1.0 / dt)
    fig, (ax1, ax2) = plt.subplots(nrows=2)
    ax1.plot(t, x)
    Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)
    return matplotlib_to_svg(fig)
