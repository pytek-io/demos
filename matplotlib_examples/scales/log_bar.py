"""
=======
Log Bar
=======

Plotting a bar chart with a logarithmic y-axis.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/scales/log_bar.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    data = (3, 1000), (10, 3), (100, 30), (500, 800), (50, 1)
    dim = len(data[0])
    w = 0.75
    dimw = w / dim
    fig, ax = plt.subplots()
    x = np.arange(len(data))
    for i in range(len(data[0])):
        y = [d[i] for d in data]
        b = ax.bar(x + i * dimw, y, dimw, bottom=0.001)
    ax.set_xticks(x + dimw / 2, labels=map(str, x))
    ax.set_yscale("log")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    return matplotlib_to_svg(fig)
