from reflect_html import *
from reflect_antd import Avatar
from reflect_ant_icons import AntDesignOutlined


def app():
    return Avatar(
        size=dict(xs=24, sm=32, md=40, lg=64, xl=80, xxl=100),
        icon=AntDesignOutlined([]),
    )
