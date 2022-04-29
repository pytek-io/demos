import matplotlib
matplotlib.use("Agg")  # this is stop Python rocket from showing in Dock on Mac

import matplotlib.pyplot as plt
from reflect_html import div
from demos.charts.utils import matplotlib_to_svg
import seaborn as sns
sns.set()

import numpy as np
import pandas as pd


def app():
    rng = np.random.RandomState(0)
    x = np.linspace(0, 10, 500)
    y = np.cumsum(rng.randn(500, 6), 0)
    plt.plot(x, y)
    plt.legend('ABCDEF', ncol=2, loc='upper left')
    return matplotlib_to_svg(plt)
