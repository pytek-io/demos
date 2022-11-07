import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

from demos.charts.utils import matplotlib_to_svg

sns.set()
import numpy as np


def app():
    plt.clf()
    rng = np.random.RandomState(0)
    x = np.linspace(0, 10, 500)
    y = np.cumsum(rng.randn(500, 6), 0)
    plt.plot(x, y)
    plt.legend("ABCDEF", ncol=2, loc="upper left")
    return matplotlib_to_svg(plt)
