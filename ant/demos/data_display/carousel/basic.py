from reflect_html import *
from reflect_antd import Carousel
from reflect import Callback

contentStyle = {
    "height": "160px",
    "color": "#fff",
    "lineHeight": "160px",
    "textAlign": "center",
    "background": "#364d79",
}


def app():

    return Carousel(
        [
            div(h3("1", style=contentStyle)),
            div(h3("2", style=contentStyle)),
            div(h3("3", style=contentStyle)),
            div(h3("4", style=contentStyle)),
        ],
        afterChange=Callback(print),
    )
