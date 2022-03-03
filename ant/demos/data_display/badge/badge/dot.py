from reflect_html import *
from reflect_antd import Badge
from reflect_ant_icons import NotificationOutlined


def app():
    return div(
        [
            Badge(NotificationOutlined(), dot=True),
            Badge(NotificationOutlined(), count=0, dot=True),
            Badge(a("Link something", href="#"), dot=True),
        ]
    )
