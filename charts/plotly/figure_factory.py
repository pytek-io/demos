from reflect_plotly import Graph
import numpy as np
import plotly.figure_factory as ff


def app():
    x1, y1 = np.meshgrid(np.arange(0, 2, 0.2), np.arange(0, 2, 0.2))
    u1 = np.cos(x1) * y1
    v1 = np.sin(x1) * y1
    return Graph(ff.create_quiver(x1, y1, u1, v1))
