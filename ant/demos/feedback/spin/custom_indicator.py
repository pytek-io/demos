from reflect_html import *
from reflect_antd import Spin
from reflect_ant_icons import LoadingOutlined


def app():
    return Spin(indicator=LoadingOutlined(style={"fontSize": 24}))
