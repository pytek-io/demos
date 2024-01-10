"""
=================
Date Demo Convert
=================


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/ticks/date_demo_convert.py.
"""
import matplotlib

matplotlib.use("Agg")
import datetime

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import DateFormatter, DayLocator, HourLocator, drange

from demos.charts.utils import matplotlib_to_svg


def app(_):
    date1 = datetime.datetime(2000, 3, 2)
    date2 = datetime.datetime(2000, 3, 6)
    delta = datetime.timedelta(hours=6)
    dates = drange(date1, date2, delta)
    y = np.arange(len(dates))
    fig, ax = plt.subplots()
    ax.plot(dates, y**2, "o")
    ax.set_xlim(dates[0], dates[-1])
    ax.xaxis.set_major_locator(DayLocator())
    ax.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))
    ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
    ax.fmt_xdata = DateFormatter("%Y-%m-%d %H:%M:%S")
    fig.autofmt_xdate()
    return matplotlib_to_svg(fig)
