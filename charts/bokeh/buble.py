from reflect_bokeh import Figure
from bokeh.plotting import figure
import numpy as np


FAVICON = "https://static.bokeh.org/favicon/favicon-32x32.png"
TITLE = "Bokeh example"
DESCRIPTION = "Simple Bokeh plot"


def app():
    # generate some data
    N = 100
    x = np.random.random(size=N) * 100
    y = np.random.random(size=N) * 100

    # generate radii and colors based on data
    radii = y / 100 * 2
    colors = [
        "#%02x%02x%02x" % (255, int(round(value * 255 / 100)), 255) for value in y
    ]

    # create a new plot with a specific size
    p = figure(
        title="Vectorized colors and radii example",
        sizing_mode="stretch_width",
        max_width=500,
        height=250,
    )

    # add circle renderer
    p.circle(
        x,
        y,
        radius=radii,
        fill_color=colors,
        fill_alpha=0.6,
        line_color="lightgrey",
    )
    return Figure(p)
