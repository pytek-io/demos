import matplotlib
matplotlib.use("Agg")  # this is stop Python rocket from showing in Dock on Mac
import numpy as np
from reflect_antd import Slider
from reflect_html import div, img

import matplotlib.pyplot as plt

TITLE = "Matplotlib"

def expose_matplotlib(fig):
    name = "test_matplotlib.svg"
    fig.savefig(name)
    return img(src=name)


def app():
    period = Slider(defaultValue=50, min=0, max=100)

    def content():
        fig = plt.figure()
        fig.subplots_adjust(top=1.)
        ax1 = fig.add_subplot(211)
        ax1.set_ylabel("volts")
        ax1.set_title("a sine wave")
        ax1.set_xlabel("time (s)")

        t = np.arange(0.0, 1.0, 0.01)
        s = np.sin(2 * np.pi * t * period() / 100)
        ax1.plot(t, s, color="blue", lw=2)

        # Fixing random state for reproducibility
        np.random.seed(19680801)

        ax2 = fig.add_axes([0.125, 0.08, 0.7, 0.3])
        ax2.set_title("a histogram")
        ax2.hist(
            np.random.randn(1000), 50, facecolor="yellow", edgecolor="yellow"
        )
        return expose_matplotlib(fig)

    return div([period, content])
