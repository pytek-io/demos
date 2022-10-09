"""
================
Parasite Simple2
================


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/axes_grid1/parasite_simple2.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import matplotlib.transforms as mtransforms
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.parasite_axes import HostAxes


def app():
    obs = [
        ["01_S1", 3.88, 0.14, 1970, 63],
        ["01_S4", 5.6, 0.82, 1622, 150],
        ["02_S1", 2.4, 0.54, 1570, 40],
        ["03_S1", 4.1, 0.62, 2380, 170],
    ]
    fig = plt.figure()
    ax_kms = fig.add_subplot(axes_class=HostAxes, aspect=1)
    pm_to_kms = ((((1.0 / 206265.0) * 2300) * 3.085e18) / 31500000.0) / 100000.0
    aux_trans = mtransforms.Affine2D().scale(pm_to_kms, 1.0)
    ax_pm = ax_kms.twin(aux_trans)
    for (n, ds, dse, w, we) in obs:
        time = (2007 + ((10.0 + (4 / 30.0)) / 12)) - 1988.5
        v = (ds / time) * pm_to_kms
        ve = (dse / time) * pm_to_kms
        ax_kms.errorbar([v], [w], xerr=[ve], yerr=[we], color="k")
    ax_kms.axis["bottom"].set_label("Linear velocity at 2.3 kpc [km/s]")
    ax_kms.axis["left"].set_label("FWHM [km/s]")
    ax_pm.axis["top"].set_label("Proper Motion [$''$/yr]")
    ax_pm.axis["top"].label.set_visible(True)
    ax_pm.axis["right"].major_ticklabels.set_visible(False)
    ax_kms.set_xlim(950, 3700)
    ax_kms.set_ylim(950, 3100)
    return matplotlib_to_svg(fig)
