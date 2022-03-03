from reflect_html import *
from reflect_antd import Slider

style = {
    "display": "inline-block",
    "height": 300,
    "marginLeft": 70,
}

marks = {
    0: "0°C",
    26: "26°C",
    37: "37°C",
    100: {
        "style": {
            "color": "#f50",
        },
        "label": strong("100°C"),
    },
}


def app():
    return [
        div(Slider(vertical=True, defaultValue=30), style=style),
        div(
            Slider(vertical=True, range=True, step=10, defaultValue=[20, 50]),
            style=style,
        ),
        div(
            Slider(vertical=True, range=True, marks=marks, defaultValue=[26, 37]),
            style=style,
        ),
    ]
