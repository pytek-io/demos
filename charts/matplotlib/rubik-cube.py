import matplotlib

matplotlib.use("Agg")  # this is stop Python rocket from showing in Dock on Mac

import numpy as np
import matplotlib.pyplot as plt
from demos.charts.utils import matplotlib_to_svg


def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x


def app():
    N = 3
    volume = np.random.rand(N, N, N)
    filled = np.ones(
        (N, N, N),
    )

    colors = np.repeat(volume[:, :, :, np.newaxis], 1)

    # prepare some coordinates, and attach rgb values to each
    r, g, b = np.indices((4, 4, 4)) / 3.0
    rc = midpoints(r)
    gc = midpoints(g)
    bc = midpoints(b)

    # try with (4,) instead of (3,) and you will the frame
    colors = np.zeros((3, 3, 3) + (3,))
    colors[..., 0] = rc
    colors[..., 1] = gc
    colors[..., 2] = bc

    fig = plt.figure()
    ax = fig.gca(projection="3d")

    ax.voxels(filled, facecolors=colors, edgecolors="k")
    plt.title("Rubik's Cube")
    plt.gray()
    return matplotlib_to_svg(plt)
