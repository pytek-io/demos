from reflect_html import *
from reflect_antd import Popover, Button

def app():
    content = div([p("Content"), p("Content")])
    text = span("Title")
    buttonWidth = 70

    return div(
        [
            div(
                [
                    Popover(
                        Button("TL"),
                        placement="topLeft",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    Popover(
                        Button("Top"),
                        placement="top",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    Popover(
                        Button("TR"),
                        placement="topRight",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                ],
                style=dict(marginLeft=buttonWidth, whiteSpace="nowrap"),
            ),
            div(
                [
                    Popover(
                        Button("LT"),
                        placement="leftTop",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    Popover(
                        Button("Left"),
                        placement="left",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    Popover(
                        Button("LB"),
                        placement="leftBottom",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                ],
                style=dict(width=buttonWidth, float="left"),
            ),
            div(
                [
                    Popover(
                        Button("RT"),
                        placement="rightTop",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    Popover(
                        Button("Right"),
                        placement="right",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    Popover(
                        Button("RB"),
                        placement="rightBottom",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                ],
                style=dict(width=buttonWidth, marginLeft=buttonWidth * 4 + 24),
            ),
            div(
                [
                    Popover(
                        Button("BL"),
                        placement="bottomLeft",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    Popover(
                        Button("Bottom"),
                        placement="bottom",
                        title=text,
                        content=content,
                        trigger="click",
                    ),
                    Popover(
                        Button("BR"),
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
