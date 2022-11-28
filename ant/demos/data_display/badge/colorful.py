import reflect_antd as antd
import reflect_html as html


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
    return html.div(
        [
            antd.Divider("Presets", orientation="left"),
            html.div(
                [
                    html.div(antd.Badge(color=color, text=color, key=color))
                    for color in colors
                ]
            ),
            antd.Divider("Custom", orientation="left"),
            html.div(
                [
                    antd.Badge(color="#f50", text="#f50"),
                    html.br(),
                    antd.Badge(color="#2db7f5", text="#2db7f5"),
                    html.br(),
                    antd.Badge(color="#87d068", text="#87d068"),
                    html.br(),
                    antd.Badge(color="#108ee9", text="#108ee9"),
                ]
            ),
        ]
    )
