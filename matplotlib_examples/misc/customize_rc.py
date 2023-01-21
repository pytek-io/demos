"""
============
Customize Rc
============

I'm not trying to make a good looking figure here, but just to show
some examples of customizing `.rcParams` on the fly.

If you like to work interactively, and need to create different sets
of defaults for figures (e.g., one set of defaults for publication, one
set for interactive exploration), you may want to define some
functions in a custom module that set the defaults, e.g.,::

    def set_pub():
        rcParams.update({
            "font.weight": "bold",  # bold fonts
            "tick.labelsize": 15,   # large tick labels
            "lines.linewidth": 1,   # thick lines
            "lines.color": "k",     # black lines
            "grid.color": "0.5",    # gray gridlines
            "grid.linestyle": "-",  # solid gridlines
            "grid.linewidth": 0.5,  # thin gridlines
            "savefig.dpi": 300,     # higher resolution output.
        })

Then as you are working interactively, you just need to do::

    >>> set_pub()
    >>> plot([1, 2, 3])
    >>> savefig('myfig')
    >>> rcdefaults()  # restore the defaults

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/misc/customize_rc.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from demos.charts.utils import matplotlib_to_svg


def app():
    fig = plt.figure()
    plt.subplot(311)
    plt.plot([1, 2, 3])
    plt.rcParams.update(
        {
            "font.weight": "bold",
            "xtick.major.size": 5,
            "xtick.major.pad": 7,
            "xtick.labelsize": 15,
            "grid.color": "0.5",
            "grid.linestyle": "-",
            "grid.linewidth": 5,
            "lines.linewidth": 2,
            "lines.color": "g",
        }
    )
    plt.subplot(312)
    plt.plot([1, 2, 3])
    plt.grid(True)
    plt.rcdefaults()
    plt.subplot(313)
    plt.plot([1, 2, 3])
    plt.grid(True)
    return matplotlib_to_svg(fig)
