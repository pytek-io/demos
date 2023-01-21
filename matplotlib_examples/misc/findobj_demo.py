"""
============
Findobj Demo
============

Recursively find all objects that match some criteria

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/misc/findobj_demo.py.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.text as text
import numpy as np

from demos.charts.utils import matplotlib_to_svg

a = np.arange(0, 3, 0.02)
b = np.arange(0, 3, 0.02)
c = np.exp(a)
d = c[::-1]
fig, ax = plt.subplots()
plt.plot(a, c, "k--", a, d, "k:", a, c + d, "k")
plt.legend(
    ("Model length", "Data length", "Total message length"),
    loc="upper center",
    shadow=True,
)
plt.ylim([-1, 20])
plt.grid(False)
plt.xlabel("Model complexity --->")
plt.ylabel("Message length --->")
plt.title("Minimum Message Length")


def myfunc(x):
    return hasattr(x, "set_color") and not hasattr(x, "set_facecolor")


def app():
    for o in fig.findobj(myfunc):
        o.set_color("blue")
    for o in fig.findobj(text.Text):
        o.set_fontstyle("italic")
    return matplotlib_to_svg(fig)
