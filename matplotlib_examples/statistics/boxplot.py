"""
=================================
Artist customization in box plots
=================================

This example demonstrates how to use the various keyword arguments to fully
customize box plots. The first figure demonstrates how to remove and add
individual components (note that the mean is the only value not shown by
default). The second figure demonstrates how the styles of the artists can be
customized. It also demonstrates how to set the limit of the whiskers to
specific percentiles (lower right axes)

A good general reference on boxplots and their history can be found here:
https://vita.had.co.nz/papers/boxplots.pdf


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/statistics/boxplot.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    np.random.seed(19680801)
    data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
    labels = list("ABCD")
    fs = 10
    fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(6, 6), sharey=True)
    axs[0, 0].boxplot(data, labels=labels)
    axs[0, 0].set_title("Default", fontsize=fs)
    axs[0, 1].boxplot(data, labels=labels, showmeans=True)
    axs[0, 1].set_title("showmeans=True", fontsize=fs)
    axs[0, 2].boxplot(data, labels=labels, showmeans=True, meanline=True)
    axs[0, 2].set_title("showmeans=True,\nmeanline=True", fontsize=fs)
    axs[1, 0].boxplot(data, labels=labels, showbox=False, showcaps=False)
    tufte_title = "Tufte Style \n(showbox=False,\nshowcaps=False)"
    axs[1, 0].set_title(tufte_title, fontsize=fs)
    axs[1, 1].boxplot(data, labels=labels, notch=True, bootstrap=10000)
    axs[1, 1].set_title("notch=True,\nbootstrap=10000", fontsize=fs)
    axs[1, 2].boxplot(data, labels=labels, showfliers=False)
    axs[1, 2].set_title("showfliers=False", fontsize=fs)
    for ax in axs.flat:
        ax.set_yscale("log")
        ax.set_yticklabels([])
    fig.subplots_adjust(hspace=0.4)
    boxprops = {"linestyle": "--", "linewidth": 3, "color": "darkgoldenrod"}
    flierprops = {
        "marker": "o",
        "markerfacecolor": "green",
        "markersize": 12,
        "markeredgecolor": "none",
    }
    medianprops = {"linestyle": "-.", "linewidth": 2.5, "color": "firebrick"}
    meanpointprops = {
        "marker": "D",
        "markeredgecolor": "black",
        "markerfacecolor": "firebrick",
    }
    meanlineprops = {"linestyle": "--", "linewidth": 2.5, "color": "purple"}
    fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(6, 6), sharey=True)
    axs[0, 0].boxplot(data, boxprops=boxprops)
    axs[0, 0].set_title("Custom boxprops", fontsize=fs)
    axs[0, 1].boxplot(data, flierprops=flierprops, medianprops=medianprops)
    axs[0, 1].set_title("Custom medianprops\nand flierprops", fontsize=fs)
    axs[0, 2].boxplot(data, whis=(0, 100))
    axs[0, 2].set_title("whis=(0, 100)", fontsize=fs)
    axs[1, 0].boxplot(data, meanprops=meanpointprops, meanline=False, showmeans=True)
    axs[1, 0].set_title("Custom mean\nas point", fontsize=fs)
    axs[1, 1].boxplot(data, meanprops=meanlineprops, meanline=True, showmeans=True)
    axs[1, 1].set_title("Custom mean\nas line", fontsize=fs)
    axs[1, 2].boxplot(data, whis=[15, 85])
    axs[1, 2].set_title("whis=[15, 85]\n#percentiles", fontsize=fs)
    for ax in axs.flat:
        ax.set_yscale("log")
        ax.set_yticklabels([])
    fig.suptitle("I never said they'd be pretty")
    fig.subplots_adjust(hspace=0.4)
    return matplotlib_to_svg(fig)
