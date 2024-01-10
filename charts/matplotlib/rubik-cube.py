import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x


def app(_):
    N = 3
    volume = np.random.rand(N, N, N)
    filled = np.ones((N, N, N))
    colors = np.repeat(volume[:, :, :, (np.newaxis)], 1)
    r, g, b = np.indices((4, 4, 4)) / 3.0
    rc = midpoints(r)
    gc = midpoints(g)
    bc = midpoints(b)
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
