"""
==========
Table Demo
==========

Demo of table function to display a table within a plot.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/misc/table_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from demos.charts.utils import matplotlib_to_svg


def app():
    data = [
        [66386, 174296, 75131, 577908, 32015],
        [58230, 381139, 78045, 99308, 160454],
        [89135, 80552, 152558, 497981, 603535],
        [78415, 81858, 150656, 193263, 69638],
        [139361, 331509, 343164, 781380, 52269],
    ]
    columns = "Freeze", "Wind", "Flood", "Quake", "Hail"
    rows = [("%d year" % x) for x in (100, 50, 20, 10, 5)]
    values = np.arange(0, 2500, 500)
    value_increment = 1000
    colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
    n_rows = len(data)
    index = np.arange(len(columns)) + 0.3
    bar_width = 0.4
    y_offset = np.zeros(len(columns))
    fig = plt.figure()
    cell_text = []
    for row in range(n_rows):
        plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
        y_offset = y_offset + data[row]
        cell_text.append([("%1.1f" % (x / 1000.0)) for x in y_offset])
    colors = colors[::-1]
    cell_text.reverse()
    the_table = plt.table(
        cellText=cell_text,
        rowLabels=rows,
        rowColours=colors,
        colLabels=columns,
        loc="bottom",
    )
    plt.subplots_adjust(left=0.2, bottom=0.2)
    plt.ylabel("Loss in ${0}'s".format(value_increment))
    plt.yticks(values * value_increment, [("%d" % val) for val in values])
    plt.xticks([])
    plt.title("Loss by Disaster")
    return matplotlib_to_svg(fig)
