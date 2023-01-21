"""
===================================
Box plot vs. violin plot comparison
===================================

Note that although violin plots are closely related to Tukey's (1977)
box plots, they add useful information such as the distribution of the
sample data (density trace).

By default, box plots show data points outside 1.5 * the inter-quartile
range as outliers above or below the whiskers whereas violin plots show
the whole range of the data.

A good general reference on boxplots and their history can be found
here: http://vita.had.co.nz/papers/boxplots.pdf

Violin plots require matplotlib >= 1.4.

For more information on violin plots, the scikit-learn docs have a great
section: https://scikit-learn.org/stable/modules/density.html

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/statistics/boxplot_vs_violin.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))
    np.random.seed(19680801)
    all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]
    axs[0].violinplot(all_data, showmeans=False, showmedians=True)
    axs[0].set_title("Violin plot")
    axs[1].boxplot(all_data)
    axs[1].set_title("Box plot")
    for ax in axs:
        ax.yaxis.grid(True)
        ax.set_xticks(
            [(y + 1) for y in range(len(all_data))], labels=["x1", "x2", "x3", "x4"]
        )
        ax.set_xlabel("Four separate samples")
        ax.set_ylabel("Observed values")
    return matplotlib_to_svg(fig)
