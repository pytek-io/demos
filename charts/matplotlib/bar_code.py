import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg

matplotlib.use("Agg")


def app(_):
    matplotlib.rcParams["font.size"] = 8.0
    np.random.seed(19680801)
    data1 = np.random.random([6, 50])
    colors1 = ["C{}".format(i) for i in range(6)]
    lineoffsets1 = [-15, -3, 1, 1.5, 6, 10]
    linelengths1 = [5, 2, 1, 1, 3, 1.5]
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].eventplot(
        data1, colors=colors1, lineoffsets=lineoffsets1, linelengths=linelengths1
    )
    axs[1, 0].eventplot(
        data1,
        colors=colors1,
        lineoffsets=lineoffsets1,
        linelengths=linelengths1,
        orientation="vertical",
    )
    data2 = np.random.gamma(4, size=[60, 50])
    colors2 = "black"
    lineoffsets2 = 1
    linelengths2 = 1
    axs[0, 1].eventplot(
        data2, colors=colors2, lineoffsets=lineoffsets2, linelengths=linelengths2
    )
    axs[1, 1].eventplot(
        data2,
        colors=colors2,
        lineoffsets=lineoffsets2,
        linelengths=linelengths2,
        orientation="vertical",
    )
    return matplotlib_to_svg(fig)
