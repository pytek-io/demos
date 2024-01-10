"""
=============
Multipage PDF
=============

This is a demo of creating a pdf file with several pages,
as well as adding metadata and annotations to pdf files.

If you want to use a multipage pdf file using LaTeX, you need
to use ``from matplotlib.backends.backend_pgf import PdfPages``.
This version however does not support `.attach_note`.

This example has been taken from https://github.com/matplotlib/matplotlib/blob/main/matplotlib/examples/misc/multipage_pdf.py.
"""
import matplotlib

matplotlib.use("Agg")
import datetime

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

from demos.charts.utils import matplotlib_to_svg


def app(_):
    with PdfPages("multipage_pdf.pdf") as pdf:
        plt.figure(figsize=(3, 3))
        plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], "r-o")
        plt.title("Page One")
        pdf.savefig()
        plt.close()
        plt.rcParams["text.usetex"] = True
        plt.figure(figsize=(8, 6))
        x = np.arange(0, 5, 0.1)
        plt.plot(x, np.sin(x), "b-")
        plt.title("Page Two")
        pdf.attach_note("plot of sin(x)")
        pdf.savefig()
        plt.close()
        plt.rcParams["text.usetex"] = False
        fig = plt.figure(figsize=(4, 5))
        plt.plot(x, x**2, "ko")
        plt.title("Page Three")
        pdf.savefig(fig)
        plt.close()
        d = pdf.infodict()
        d["Title"] = "Multipage PDF Example"
        d["Author"] = "Jouni K. Seppänen"
        d["Subject"] = "How to create a multipage pdf file and set its metadata"
        d["Keywords"] = "PdfPages multipage keywords author title subject"
        d["CreationDate"] = datetime.datetime(2009, 11, 13)
        d["ModDate"] = datetime.datetime.today()
    return matplotlib_to_svg(fig)
