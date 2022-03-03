from reflect_html import *
from reflect_antd import Badge
from reflect_ant_icons import ClockCircleOutlined


def app():
    return div(
        [
            Badge(a(href="#", className="head-example"), count=5),
            Badge(a(href="#", className="head-example"), count=0, showZero=True),
            Badge(
                a(href="#", className="head-example"),
                count=ClockCircleOutlined(style=dict(color="#f5222d")),
            ),
        ]
    )
