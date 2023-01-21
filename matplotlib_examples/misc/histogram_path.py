"""
========================================================
Building histograms using Rectangles and PolyCollections
========================================================

Using a path patch to draw rectangles.
The technique of using lots of Rectangle instances, or
the faster method of using PolyCollections, were implemented before we
had proper paths with moveto/lineto, closepoly etc in mpl.  Now that
we have them, we can draw collections of regularly shaped objects with
homogeneous properties more efficiently with a PathCollection. This
example makes a histogram -- it's more work to set up the vertex arrays
at the outset, but it should be much faster for large numbers of
objects.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/misc/histogram_path.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    fig, ax = plt.subplots()
    np.random.seed(19680801)
    data = np.random.randn(1000)
    n, bins = np.histogram(data, 50)
    left = bins[:-1]
    right = bins[1:]
    bottom = np.zeros(len(left))
    top = bottom + n
    XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T
    barpath = path.Path.make_compound_path_from_polys(XY)
    patch = patches.PathPatch(barpath)
    ax.add_patch(patch)
    ax.set_xlim(left[0], right[-1])
    ax.set_ylim(bottom.min(), top.max())
    nrects = len(left)
    nverts = nrects * (1 + 3 + 1)
    verts = np.zeros((nverts, 2))
    codes = np.ones(nverts, int) * path.Path.LINETO
    codes[0::5] = path.Path.MOVETO
    codes[4::5] = path.Path.CLOSEPOLY
    verts[0::5, (0)] = left
    verts[0::5, (1)] = bottom
    verts[1::5, (0)] = left
    verts[1::5, (1)] = top
    verts[2::5, (0)] = right
    verts[2::5, (1)] = top
    verts[3::5, (0)] = right
    verts[3::5, (1)] = bottom
    barpath = path.Path(verts, codes)
    return matplotlib_to_svg(fig)
