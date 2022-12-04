import reflect_antd as antd
import reflect_html as html


def app():
    content = html.div([html.p("Content"), html.p("Content")])
    text = html.span("Title")
    buttonWidth = 70
    return html.div(
        [
            html.div(
                [
                    antd.Popover(
                        antd.Button("TL"),
                        placement="topLeft",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    antd.Popover(
                        antd.Button("Top"),
                        placement="top",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    antd.Popover(
                        antd.Button("TR"),
                        placement="topRight",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                ],
                style=dict(marginLeft=buttonWidth, whiteSpace="nowrap"),
            ),
            html.div(
                [
                    antd.Popover(
                        antd.Button("LT"),
                        placement="leftTop",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    antd.Popover(
                        antd.Button("Left"),
                        placement="left",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    antd.Popover(
                        antd.Button("LB"),
                        placement="leftBottom",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                ],
                style=dict(width=buttonWidth, float="left"),
            ),
            html.div(
                [
                    antd.Popover(
                        antd.Button("RT"),
                        placement="rightTop",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    antd.Popover(
                        antd.Button("Right"),
                        placement="right",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    antd.Popover(
                        antd.Button("RB"),
                        placement="rightBottom",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                ],
                style=dict(width=buttonWidth, marginLeft=buttonWidth * 4 + 24),
            ),
            html.div(
                [
                    antd.Popover(
                        antd.Button("BL"),
                        placement="bottomLeft",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    antd.Popover(
                        antd.Button("Bottom"),
                        placement="bottom",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    antd.Popover(
                        antd.Button("BR"),
                        placement="bottomRight",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                ],
                style=dict(marginLeft=buttonWidth, clear="both", whiteSpace="nowrap"),
            ),
        ],
        className="demo",
    )
