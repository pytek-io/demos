"""
=======================================================
Controlling style of text and labels using a dictionary
=======================================================

This example shows how to share parameters across many text objects and labels
by creating a dictionary of options passed across several functions.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/text_labels_and_annotations/text_fontdict.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    font = {"family": "serif", "color": "darkred", "weight": "normal", "size": 16}
    x = np.linspace(0.0, 5.0, 100)
    y = np.cos(2 * np.pi * x) * np.exp(-x)
    fig = plt.figure()
    plt.plot(x, y, "k")
    plt.title("Damped exponential decay", fontdict=font)
    plt.text(2, 0.65, "$\\cos(2 \\pi t) \\exp(-t)$", fontdict=font)
    plt.xlabel("time (s)", fontdict=font)
    plt.ylabel("voltage (mV)", fontdict=font)
    plt.subplots_adjust(left=0.15)
    return matplotlib_to_svg(fig)
