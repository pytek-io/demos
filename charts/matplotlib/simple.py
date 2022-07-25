import matplotlib

matplotlib.use("Agg")  # this is stop Python rocket from showing in Dock on Mac
from importlib import reload
from io import StringIO

import demos.charts.matplotlib.methods as methods
import numpy as np
from reflect import Controller
from reflect_antd import Button, Slider
from reflect_html import div, inline_svg

import matplotlib.pyplot as plt

TITLE = "Matplotlib"


def matplotlib_to_svg(fig):
    content = StringIO()
    fig.savefig(content, format="svg")
    return inline_svg(content.getvalue())


def app():
    period = Slider(defaultValue=50, min=0, max=100)

    def content():
        reload(methods) # reloading code changes without restarting the process
        x = np.linspace(0, 2 * np.pi, 400)
        y = methods.method1(x**2, period())
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

        # Hide x labels and tick labels for top plots and y ticks for right plots.
        for ax in axs.flat:
            ax.label_outer()
        return matplotlib_to_svg(fig)

    with Controller() as controller:
        return div(
            [
                content,
                period,
                div(
                    [
                        Button("Update", onClick=controller.commit),
                    ],
                    style={"margin": "auto"},
                ),
            ],
            style={"width": "100%", "display": "grid", "justify-content": "center"},
        )
