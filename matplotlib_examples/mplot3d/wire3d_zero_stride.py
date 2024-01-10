"""
===================================
3D wireframe plots in one direction
===================================

Demonstrates that setting rstride or cstride to 0 causes wires to not be
generated in the corresponding direction.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/wire3d_zero_stride.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

from demos.charts.utils import matplotlib_to_svg


def app(_):
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(8, 12), subplot_kw={"projection": "3d"}
    )
    X, Y, Z = axes3d.get_test_data(0.05)
    ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
    ax1.set_title("Column (x) stride set to 0")
    ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=10)
    ax2.set_title("Row (y) stride set to 0")
    plt.tight_layout()
    return matplotlib_to_svg(fig)
