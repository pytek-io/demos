from reflect_html import *
from reflect_antd import Carousel, Radio


def app():
    contentStyle = {
        "height": "160px",
        "color": "#fff",
        "lineHeight": "160px",
        "textAlign": "center",
        "background": "#364d79",
    }

    dotPosition = Radio.Group(
        [
            Radio.Button("Top", value="top"),
            Radio.Button("Bottom", value="bottom"),
            Radio.Button("Left", value="left"),
            Radio.Button("Right", value="right"),
        ],
        style=dict(marginBottom=8),
    )
    return div(
        [
            dotPosition,
            Carousel(
                [
                    div(h3("1", style=contentStyle)),
                    div(h3("2", style=contentStyle)),
                    div(h3("3", style=contentStyle)),
                    div(h3("4", style=contentStyle)),
                ],
                dotPosition=dotPosition,
            ),
        ]
    )
