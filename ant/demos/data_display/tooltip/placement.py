from reflect_html import *
from reflect_antd import Tooltip, Button


def app():
    text = span("prompt text")
    buttonWidth = 70
    return div(
        [
            div(
                [
                    Tooltip(Button("TL"), placement="topLeft", title=text),
                    Tooltip(Button("Top"), placement="top", title=text),
                    Tooltip(Button("TR"), placement="topRight", title=text),
                ],
                style=dict(marginLeft=buttonWidth, whiteSpace="nowrap"),
            ),
            div(
                [
                    Tooltip(Button("LT"), placement="leftTop", title=text),
                    Tooltip(Button("Left"), placement="left", title=text),
                    Tooltip(Button("LB"), placement="leftBottom", title=text),
                ],
                style=dict(width=buttonWidth, float="left"),
            ),
            div(
                [
                    Tooltip(Button("RT"), placement="rightTop", title=text),
                    Tooltip(Button("Right"), placement="right", title=text),
                    Tooltip(Button("RB"), placement="rightBottom", title=text),
                ],
                style=dict(width=buttonWidth, marginLeft=buttonWidth * 4 + 24),
            ),
            div(
                [
                    Tooltip(Button("BL"), placement="bottomLeft", title=text),
                    Tooltip(Button("Bottom"), placement="bottom", title=text),
                    Tooltip(Button("BR"), placement="bottomRight", title=text),
                ],
                style=dict(marginLeft=buttonWidth, clear="both", whiteSpace="nowrap"),
            ),
        ],
        className="demo",
    )
