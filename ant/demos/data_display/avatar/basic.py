from reflect_html import *
from reflect_antd import Avatar
from reflect_ant_icons import UserOutlined


def app():
    return [
        div(
            [
                Avatar(size=64, icon=UserOutlined([])),
                Avatar(size="large", icon=UserOutlined([])),
                Avatar(icon=UserOutlined([])),
                Avatar(size="small", icon=UserOutlined([])),
            ]
        ),
        div(
            [
                Avatar(shape="square", size=64, icon=UserOutlined([])),
                Avatar(shape="square", size="large", icon=UserOutlined([])),
                Avatar(shape="square", icon=UserOutlined([])),
                Avatar(shape="square", size="small", icon=UserOutlined([])),
            ]
        ),
    ]
