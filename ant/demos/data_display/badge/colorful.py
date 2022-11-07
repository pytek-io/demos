from reflect_html import *
from reflect_antd import Badge, Divider


def app():
    colors = [
        "pink",
        "red",
        "yellow",
        "orange",
        "cyan",
        "green",
        "blue",
        "purple",
        "geekblue",
        "magenta",
        "volcano",
        "gold",
        "lime",
    ]
    return div(
        [
            Divider("Presets", orientation="left"),
            div([div(Badge(color=color, text=color, key=color)) for color in colors]),
            Divider("Custom", orientation="left"),
            div(
                [
                    Badge(color="#f50", text="#f50"),
                    br(),
                    Badge(color="#2db7f5", text="#2db7f5"),
                    br(),
                    Badge(color="#87d068", text="#87d068"),
                    br(),
                    Badge(color="#108ee9", text="#108ee9"),
                ]
            ),
        ]
    )
