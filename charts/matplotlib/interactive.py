import matplotlib

matplotlib.use("Agg")
import importlib

import matplotlib.pyplot as plt
import numpy as np
import render as r
import render_antd as antd
import render_html as html

import demos.charts.matplotlib.methods as methods
from demos.charts.utils import matplotlib_to_svg

TITLE = "Matplotlib"


def app(_):
    with r.Controller() as controller:
        period = antd.Slider(defaultValue=50, min=0, max=100)

    def content():
        importlib.reload(methods)
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
            ax.label_outer()
        return matplotlib_to_svg(fig)

    return html.div(
        [
            content,
            period,
            html.div(
                [antd.Button("Update", onClick=controller.commit)],
                style={"margin": "auto"},
            ),
        ],
        style={"width": "100%", "display": "grid", "justify-content": "center"},
    )
