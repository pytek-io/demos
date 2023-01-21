"""
====================
Usetex Baseline Test
====================

Comparison of text baselines computed for mathtext and usetex.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/text_labels_and_annotations/usetex_baseline_test.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def app():
    plt.rcParams.update({"mathtext.fontset": "cm", "mathtext.rm": "serif"})
    fig = plt.figure(figsize=(2 * 3, 6.5))
    axs = fig.subplots(1, 2)
    for ax, usetex in zip(axs, [False, True]):
        ax.axvline(0, color="r")
        test_strings = ["lg", "$\\frac{1}{2}\\pi$", "$p^{3^A}$", "$p_{3_2}$"]
        for i, s in enumerate(test_strings):
            ax.axhline(i, color="r")
            ax.text(
                0.0,
                3 - i,
                s,
                usetex=usetex,
                verticalalignment="baseline",
                size=50,
                bbox={"pad": 0, "ec": "k", "fc": "none"},
            )
        ax.set(
            xlim=(-0.1, 1.1),
            ylim=(-0.8, 3.9),
            xticks=[],
            yticks=[],
            title=f"usetex={usetex}\n",
        )
    return matplotlib_to_svg(fig)
