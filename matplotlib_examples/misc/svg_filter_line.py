"""
===============
SVG Filter Line
===============

Demonstrate SVG filtering effects which might be used with Matplotlib.

Note that the filtering effects are only effective if your SVG renderer
support it.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/misc/svg_filter_line.py.
"""
import matplotlib

matplotlib.use("Agg")
import io
import xml.etree.ElementTree as ET

import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms

from demos.charts.utils import matplotlib_to_svg


def app():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    (l1,) = ax.plot(
        [0.1, 0.5, 0.9], [0.1, 0.9, 0.5], "bo-", mec="b", lw=5, ms=10, label="Line 1"
    )
    (l2,) = ax.plot(
        [0.1, 0.5, 0.9], [0.5, 0.2, 0.7], "rs-", mec="r", lw=5, ms=10, label="Line 2"
    )
    for l in [l1, l2]:
        xx = l.get_xdata()
        yy = l.get_ydata()
        (shadow,) = ax.plot(xx, yy)
        shadow.update_from(l)
        shadow.set_color("0.2")
        shadow.set_zorder(l.get_zorder() - 0.5)
        transform = mtransforms.offset_copy(
            l.get_transform(), fig, x=4.0, y=-6.0, units="points"
        )
        shadow.set_transform(transform)
        shadow.set_gid(l.get_label() + "_shadow")
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
    f = io.BytesIO()
    plt.savefig(f, format="svg")
    filter_def = """
  <defs xmlns='http://www.w3.org/2000/svg'
        xmlns:xlink='http://www.w3.org/1999/xlink'>
    <filter id='dropshadow' height='1.2' width='1.2'>
      <feGaussianBlur result='blur' stdDeviation='3'/>
    </filter>
  </defs>
"""
    tree, xmlid = ET.XMLID(f.getvalue())
    tree.insert(0, ET.XML(filter_def))
    for l in [l1, l2]:
        shadow = xmlid[l.get_label() + "_shadow"]
        shadow.set("filter", "url(#dropshadow)")
    fn = "svg_filter_line.svg"
    print(f"Saving '{fn}'")
    ET.ElementTree(tree).write(fn)
    return matplotlib_to_svg(fig)
