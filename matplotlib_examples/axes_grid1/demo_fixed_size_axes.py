"""
===============================
Axes with a fixed physical size
===============================

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/demo_fixed_size_axes.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import Divider, Size

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig = plt.figure(figsize=(6, 6))
    h = [Size.Fixed(1.0), Size.Fixed(4.5)]
    v = [Size.Fixed(0.7), Size.Fixed(5.0)]
    divider = Divider(fig, (0, 0, 1, 1), h, v, aspect=False)
    ax = fig.add_axes(
        divider.get_position(), axes_locator=divider.new_locator(nx=1, ny=1)
    )
    ax.plot([1, 2, 3])
    fig = plt.figure(figsize=(6, 6))
    h = [Size.Fixed(1.0), Size.Scaled(1.0), Size.Fixed(0.2)]
    v = [Size.Fixed(0.7), Size.Scaled(1.0), Size.Fixed(0.5)]
    divider = Divider(fig, (0, 0, 1, 1), h, v, aspect=False)
    ax = fig.add_axes(
        divider.get_position(), axes_locator=divider.new_locator(nx=1, ny=1)
    )
    ax.plot([1, 2, 3])
    return matplotlib_to_svg(fig)
