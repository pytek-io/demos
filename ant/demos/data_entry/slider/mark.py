from reflect_html import *
from reflect_antd import Slider

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
        h4("included=true"),
        Slider(marks=marks, defaultValue=37),
        Slider(range=True, marks=marks, defaultValue=[26, 37]),
        h4("included=false"),
        Slider(marks=marks, included=False, defaultValue=37),
        h4("marks & step"),
        Slider(marks=marks, step=10, defaultValue=37),
        h4("step=null"),
        Slider(marks=marks, step=None, defaultValue=37),
    ]
