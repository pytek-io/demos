import render_antd as antd
import render_html as html


def app():
    contentStyle = {
        "height": "160px",
        "color": "#fff",
        "lineHeight": "160px",
        "textAlign": "center",
        "background": "#364d79",
    }
    dotPosition = antd.Radio.Group(
        [
            antd.Radio.Button("Top", value="top"),
            antd.Radio.Button("Bottom", value="bottom"),
            antd.Radio.Button("Left", value="left"),
            antd.Radio.Button("Right", value="right"),
        ],
        style={"marginBottom": 8},
    )
    return html.div(
        [
            dotPosition,
            antd.Carousel(
                [
                    html.div(html.h3("1", style=contentStyle)),
                    html.div(html.h3("2", style=contentStyle)),
                    html.div(html.h3("3", style=contentStyle)),
                    html.div(html.h3("4", style=contentStyle)),
                ],
                dotPosition=dotPosition,
            ),
        ]
    )
