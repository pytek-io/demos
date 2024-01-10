"""
============
Boxplot Demo
============

Example boxplot code

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/pyplots/boxplot_demo_pyplot.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    np.random.seed(19680801)
    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    data = np.concatenate((spread, center, flier_high, flier_low))
    fig1, ax1 = plt.subplots()
    ax1.set_title("Basic Plot")
    ax1.boxplot(data)
    fig2, ax2 = plt.subplots()
    ax2.set_title("Notched boxes")
    ax2.boxplot(data, notch=True)
    green_diamond = {"markerfacecolor": "g", "marker": "D"}
    fig3, ax3 = plt.subplots()
    ax3.set_title("Changed Outlier Symbols")
    ax3.boxplot(data, flierprops=green_diamond)
    fig4, ax4 = plt.subplots()
    ax4.set_title("Hide Outlier Points")
    ax4.boxplot(data, showfliers=False)
    red_square = {"markerfacecolor": "r", "marker": "s"}
    fig5, ax5 = plt.subplots()
    ax5.set_title("Horizontal Boxes")
    ax5.boxplot(data, vert=False, flierprops=red_square)
    fig6, ax6 = plt.subplots()
    ax6.set_title("Shorter Whisker Length")
    ax6.boxplot(data, flierprops=red_square, vert=False, whis=0.75)
    spread = np.random.rand(50) * 100
    center = np.ones(25) * 40
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    d2 = np.concatenate((spread, center, flier_high, flier_low))
    data = [data, d2, d2[::2]]
    fig, ax7 = plt.subplots()
    ax7.set_title("Multiple Samples with Different sizes")
    ax7.boxplot(data)
    return matplotlib_to_svg(fig)
