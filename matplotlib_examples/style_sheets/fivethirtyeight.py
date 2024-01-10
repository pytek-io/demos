"""
===========================
FiveThirtyEight style sheet
===========================

This shows an example of the "fivethirtyeight" styling, which
tries to replicate the styles from FiveThirtyEight.com.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/style_sheets/fivethirtyeight.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    plt.style.use("fivethirtyeight")
    x = np.linspace(0, 10)
    np.random.seed(19680801)
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x) + x + np.random.randn(50))
    ax.plot(x, np.sin(x) + 0.5 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) + 2 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) - 0.5 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) - 2 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) + np.random.randn(50))
    ax.set_title("'fivethirtyeight' style sheet")
    return matplotlib_to_svg(fig)
