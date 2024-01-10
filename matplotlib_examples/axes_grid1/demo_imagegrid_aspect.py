"""
=========================================
Setting a fixed aspect on ImageGrid cells
=========================================

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/demo_imagegrid_aspect.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig = plt.figure()
    grid1 = ImageGrid(fig, 121, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
    for i in [0, 1]:
        grid1[i].set_aspect(2)
    grid2 = ImageGrid(fig, 122, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
    for i in [1, 3]:
        grid2[i].set_aspect(2)
    return matplotlib_to_svg(fig)
