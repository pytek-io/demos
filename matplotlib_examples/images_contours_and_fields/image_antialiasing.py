"""
==================
Image antialiasing
==================

Images are represented by discrete pixels, either on the screen or in an
image file.  When data that makes up the image has a different resolution
than its representation on the screen we will see aliasing effects.  How
noticeable these are depends on how much down-sampling takes place in
the change of resolution (if any).

When subsampling data, aliasing is reduced by smoothing first and then
subsampling the smoothed data.  In Matplotlib, we can do that
smoothing before mapping the data to colors, or we can do the smoothing
on the RGB(A) data in the final image.  The difference between these is
shown below, and controlled with the *interpolation_stage* keyword argument.

The default image interpolation in Matplotlib is 'antialiased', and
it is applied to the data.  This uses a
hanning interpolation on the data provided by the user for reduced aliasing
in most situations. Only when there is upsampling by a factor of 1, 2 or
>=3 is 'nearest' neighbor interpolation used.

Other anti-aliasing filters can be specified in `.Axes.imshow` using the
*interpolation* keyword argument.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/images_contours_and_fields/image_antialiasing.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import numpy as np
import matplotlib.pyplot as plt


def app():
    N = 450
    x = (np.arange(N) / N) - 0.5
    y = (np.arange(N) / N) - 0.5
    aa = np.ones((N, N))
    aa[::2, :] = -1
    (X, Y) = np.meshgrid(x, y)
    R = np.sqrt(((X**2) + (Y**2)))
    f0 = 5
    k = 100
    a = np.sin(((np.pi * 2) * ((f0 * R) + ((k * (R**2)) / 2))))
    a[: int((N / 2)), :][(R[: int((N / 2)), :] < 0.4)] = -1
    a[: int((N / 2)), :][(R[: int((N / 2)), :] < 0.3)] = 1
    aa[:, int((N / 3)) :] = a[:, int((N / 3)) :]
    a = aa
    (fig, axs) = plt.subplots(2, 2, figsize=(5, 6), constrained_layout=True)
    axs[(0, 0)].imshow(a, interpolation="nearest", cmap="RdBu_r")
    axs[(0, 0)].set_xlim(100, 200)
    axs[(0, 0)].set_ylim(275, 175)
    axs[(0, 0)].set_title("Zoom")
    for (ax, interp, space) in zip(
        axs.flat[1:],
        ["nearest", "antialiased", "antialiased"],
        ["data", "data", "rgba"],
    ):
        ax.imshow(a, interpolation=interp, interpolation_stage=space, cmap="RdBu_r")
        ax.set_title(f"interpolation='{interp}' space='{space}'")
    (fig, ax) = plt.subplots(figsize=(6.8, 6.8))
    ax.imshow(a, interpolation="nearest", cmap="gray")
    ax.set_title("upsampled by factor a 1.048, interpolation='nearest'")
    (fig, ax) = plt.subplots(figsize=(6.8, 6.8))
    ax.imshow(a, interpolation="antialiased", cmap="gray")
    ax.set_title("upsampled by factor a 1.048, interpolation='antialiased'")
    (fig, axs) = plt.subplots(1, 2, figsize=(7, 4), constrained_layout=True)
    for (ax, interp) in zip(axs, ["hanning", "lanczos"]):
        ax.imshow(a, interpolation=interp, cmap="gray")
        ax.set_title(f"interpolation='{interp}'")
    return matplotlib_to_svg(fig)
