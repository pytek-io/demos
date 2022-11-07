from reflect_html import *
from reflect_antd import Rate
from reflect_ant_icons import HeartOutlined


def app():
    return div(
        [
            Rate(character=HeartOutlined([]), allowHalf=True),
            br(),
            Rate(character="A", allowHalf=True, style=dict(fontSize=36)),
            br(),
            Rate(character="好", allowHalf=True),
        ]
    )
