import render_antd as antd
import render_html as html


def app(_):
    text = html.span("prompt text")
    buttonWidth = 70
    return html.div(
        [
            html.div(
                [
                    antd.Tooltip(antd.Button("TL"), placement="topLeft", title=text),
                    antd.Tooltip(antd.Button("Top"), placement="top", title=text),
                    antd.Tooltip(antd.Button("TR"), placement="topRight", title=text),
                ],
                style={"marginLeft": buttonWidth, "whiteSpace": "nowrap"},
            ),
            html.div(
                [
                    antd.Tooltip(antd.Button("LT"), placement="leftTop", title=text),
                    antd.Tooltip(antd.Button("Left"), placement="left", title=text),
                    antd.Tooltip(antd.Button("LB"), placement="leftBottom", title=text),
                ],
                style={"width": buttonWidth, "float": "left"},
            ),
            html.div(
                [
                    antd.Tooltip(antd.Button("RT"), placement="rightTop", title=text),
                    antd.Tooltip(antd.Button("Right"), placement="right", title=text),
                    antd.Tooltip(
                        antd.Button("RB"), placement="rightBottom", title=text
                    ),
                ],
                style={"width": buttonWidth, "marginLeft": buttonWidth * 4 + 24},
            ),
            html.div(
                [
                    antd.Tooltip(antd.Button("BL"), placement="bottomLeft", title=text),
                    antd.Tooltip(antd.Button("Bottom"), placement="bottom", title=text),
                    antd.Tooltip(
                        antd.Button("BR"), placement="bottomRight", title=text
                    ),
                ],
                style={
                    "marginLeft": buttonWidth,
                    "clear": "both",
                    "whiteSpace": "nowrap",
                },
            ),
        ],
        className="demo",
    )
