"""
================
Lorenz Attractor
================

This is an example of plotting Edward Lorenz's 1963 `"Deterministic Nonperiodic
Flow"`_ in a 3-dimensional space using mplot3d.

.. _"Deterministic Nonperiodic Flow":
   https://journals.ametsoc.org/view/journals/atsc/20/2/1520-0469_1963_020_0130_dnf_2_0_co_2.xml

.. note::
   Because this is a simple non-linear ODE, it would be more easily done using
   SciPy's ODE solver, but this approach depends only upon NumPy.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/mplot3d/lorenz_attractor.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def lorenz(xyz, *, s=10, r=28, b=2.667):
    """
    Parameters
    ----------
    xyz : array-like, shape (3,)
       Point of interest in three dimensional space.
    s, r, b : float
       Parameters defining the Lorenz attractor.

    Returns
    -------
    xyz_dot : array, shape (3,)
       Values of the Lorenz attractor's partial derivatives at *xyz*.
    """
    (x, y, z) = xyz
    x_dot = s * (y - x)
    y_dot = ((r * x) - y) - (x * z)
    z_dot = (x * y) - (b * z)
    return np.array([x_dot, y_dot, z_dot])


def app():
    dt = 0.01
    num_steps = 10000
    xyzs = np.empty(((num_steps + 1), 3))
    xyzs[0] = (0.0, 1.0, 1.05)
    for i in range(num_steps):
        xyzs[(i + 1)] = xyzs[i] + (lorenz(xyzs[i]) * dt)
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot(*xyzs.T, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    return matplotlib_to_svg(fig)