from reflect_html import *
from reflect_antd import Avatar, Badge
from reflect_ant_icons import UserOutlined


def app():
    return [
        span(
            Badge(Avatar(shape="square", icon=UserOutlined([])), count=1),
            className="avatar-item",
        ),
        span(Badge(Avatar(shape="square", icon=UserOutlined([])), dot=True)),
    ]
