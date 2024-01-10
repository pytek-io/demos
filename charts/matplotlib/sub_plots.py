import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg

matplotlib.use("Agg")


def app(_):
    plt.clf()
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x**2 / 50)
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(x, y)
    axs[0, 0].set_title("Axis [0, 0]")
    axs[0, 1].plot(x, y, "tab:orange")
    axs[0, 1].set_title("Axis [0, 1]")
    axs[1, 0].plot(x, -y, "tab:green")
    axs[1, 0].set_title("Axis [1, 0]")
    axs[1, 1].plot(x, -y, "tab:red")
    axs[1, 1].set_title("Axis [1, 1]")
    for ax in axs.flat:
        ax.set(xlabel="x-label", ylabel="y-label")
        ax.label_outer()
    return matplotlib_to_svg(fig)
