"""
================================================
Formatting date ticks using ConciseDateFormatter
================================================

Finding good tick values and formatting the ticks for an axis that
has date data is often a challenge.  `~.dates.ConciseDateFormatter` is
meant to improve the strings chosen for the ticklabels, and to minimize
the strings used in those tick labels as much as possible.

.. note::

    This formatter is a candidate to become the default date tick formatter
    in future versions of Matplotlib.  Please report any issues or
    suggestions for improvement to the github repository or mailing list.


This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/ticks/date_concise_formatter.py.
"""

import matplotlib

matplotlib.use("Agg")  # this stops Python rocket from showing up in Mac Dock
from demos.charts.utils import matplotlib_to_svg

import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import matplotlib.units as munits
import datetime


def app():
    base = datetime.datetime(2005, 2, 1)
    dates = [(base + datetime.timedelta(hours=(2 * i))) for i in range(732)]
    N = len(dates)
    np.random.seed(19680801)
    y = np.cumsum(np.random.randn(N))
    (fig, axs) = plt.subplots(3, 1, constrained_layout=True, figsize=(6, 6))
    lims = [
        (np.datetime64("2005-02"), np.datetime64("2005-04")),
        (np.datetime64("2005-02-03"), np.datetime64("2005-02-15")),
        (np.datetime64("2005-02-03 11:00"), np.datetime64("2005-02-04 13:20")),
    ]
    for (nn, ax) in enumerate(axs):
        ax.plot(dates, y)
        ax.set_xlim(lims[nn])
        for label in ax.get_xticklabels():
            label.set_rotation(40)
            label.set_horizontalalignment("right")
    axs[0].set_title("Default Date Formatter")
    (fig, axs) = plt.subplots(3, 1, constrained_layout=True, figsize=(6, 6))
    for (nn, ax) in enumerate(axs):
        locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
        formatter = mdates.ConciseDateFormatter(locator)
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.plot(dates, y)
        ax.set_xlim(lims[nn])
    axs[0].set_title("Concise Date Formatter")
    converter = mdates.ConciseDateConverter()
    munits.registry[np.datetime64] = converter
    munits.registry[datetime.date] = converter
    munits.registry[datetime.datetime] = converter
    (fig, axs) = plt.subplots(3, 1, figsize=(6, 6), constrained_layout=True)
    for (nn, ax) in enumerate(axs):
        ax.plot(dates, y)
        ax.set_xlim(lims[nn])
    axs[0].set_title("Concise Date Formatter")
    (fig, axs) = plt.subplots(3, 1, constrained_layout=True, figsize=(6, 6))
    for (nn, ax) in enumerate(axs):
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator)
        formatter.formats = ["%y", "%b", "%d", "%H:%M", "%H:%M", "%S.%f"]
        formatter.zero_formats = [""] + formatter.formats[:(-1)]
        formatter.zero_formats[3] = "%d-%b"
        formatter.offset_formats = [
            "",
            "%Y",
            "%b %Y",
            "%d %b %Y",
            "%d %b %Y",
            "%d %b %Y %H:%M",
        ]
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.plot(dates, y)
        ax.set_xlim(lims[nn])
    axs[0].set_title("Concise Date Formatter")
    formats = ["%y", "%b", "%d", "%H:%M", "%H:%M", "%S.%f"]
    zero_formats = [""] + formats[:(-1)]
    zero_formats[3] = "%d-%b"
    offset_formats = ["", "%Y", "%b %Y", "%d %b %Y", "%d %b %Y", "%d %b %Y %H:%M"]
    converter = mdates.ConciseDateConverter(
        formats=formats, zero_formats=zero_formats, offset_formats=offset_formats
    )
    munits.registry[np.datetime64] = converter
    munits.registry[datetime.date] = converter
    munits.registry[datetime.datetime] = converter
    (fig, axs) = plt.subplots(3, 1, constrained_layout=True, figsize=(6, 6))
    for (nn, ax) in enumerate(axs):
        ax.plot(dates, y)
        ax.set_xlim(lims[nn])
    axs[0].set_title("Concise Date Formatter registered non-default")
    return matplotlib_to_svg(fig)
