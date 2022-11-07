import matplotlib

matplotlib.use("Agg")
import importlib
import io

import matplotlib.pyplot as plt
import numpy as np
import reflect as r
import reflect_antd as antd
import reflect_html as html

import demos.charts.matplotlib.methods as methods

TITLE = "Matplotlib"


def matplotlib_to_svg(fig):
    content = io.StringIO()
    fig.savefig(content, format="svg")
    return html.inline_svg(content.getvalue())


def app():
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
        for ax in axs.flat:
            ax.label_outer()
        return matplotlib_to_svg(fig)

    with r.Controller() as controller:
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
