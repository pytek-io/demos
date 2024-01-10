"""
=======================
Boxplot drawer function
=======================

This example demonstrates how to pass pre-computed box plot
statistics to the box plot drawer. The first figure demonstrates
how to remove and add individual components (note that the
mean is the only value not shown by default). The second
figure demonstrates how the styles of the artists can
be customized.

A good general reference on boxplots and their history can be found
here: http://vita.had.co.nz/papers/boxplots.pdf

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/statistics/bxp.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.cbook as cbook
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app(_):
    np.random.seed(19680801)
    data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
    labels = list("ABCD")
    stats = cbook.boxplot_stats(data, labels=labels, bootstrap=10000)
    for n in range(len(stats)):
        stats[n]["med"] = np.median(data)
        stats[n]["mean"] *= 2
    print(list(stats[0]))
    fs = 10
    fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(6, 6), sharey=True)
    axs[0, 0].bxp(stats)
    axs[0, 0].set_title("Default", fontsize=fs)
    axs[0, 1].bxp(stats, showmeans=True)
    axs[0, 1].set_title("showmeans=True", fontsize=fs)
    axs[0, 2].bxp(stats, showmeans=True, meanline=True)
    axs[0, 2].set_title("showmeans=True,\nmeanline=True", fontsize=fs)
    axs[1, 0].bxp(stats, showbox=False, showcaps=False)
    tufte_title = "Tufte Style\n(showbox=False,\nshowcaps=False)"
    axs[1, 0].set_title(tufte_title, fontsize=fs)
    axs[1, 1].bxp(stats, shownotches=True)
    axs[1, 1].set_title("notch=True", fontsize=fs)
    axs[1, 2].bxp(stats, showfliers=False)
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
        "linestyle": "none",
    }
    medianprops = {"linestyle": "-.", "linewidth": 2.5, "color": "firebrick"}
    meanpointprops = {
        "marker": "D",
        "markeredgecolor": "black",
        "markerfacecolor": "firebrick",
    }
    meanlineprops = {"linestyle": "--", "linewidth": 2.5, "color": "purple"}
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(6, 6), sharey=True)
    axs[0, 0].bxp(stats, boxprops=boxprops)
    axs[0, 0].set_title("Custom boxprops", fontsize=fs)
    axs[0, 1].bxp(stats, flierprops=flierprops, medianprops=medianprops)
    axs[0, 1].set_title("Custom medianprops\nand flierprops", fontsize=fs)
    axs[1, 0].bxp(stats, meanprops=meanpointprops, meanline=False, showmeans=True)
    axs[1, 0].set_title("Custom mean\nas point", fontsize=fs)
    axs[1, 1].bxp(stats, meanprops=meanlineprops, meanline=True, showmeans=True)
    axs[1, 1].set_title("Custom mean\nas line", fontsize=fs)
    for ax in axs.flat:
        ax.set_yscale("log")
        ax.set_yticklabels([])
    fig.suptitle("I never said they'd be pretty")
    fig.subplots_adjust(hspace=0.4)
    return matplotlib_to_svg(fig)
