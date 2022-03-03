from reflect_html import *
from reflect_antd import Breadcrumb
from reflect_ant_icons import HomeOutlined, UserOutlined


def app():
    return Breadcrumb(
        [
            Breadcrumb.Item(HomeOutlined(), href=""),
            Breadcrumb.Item([UserOutlined(), span("Application List")], href=""),
            Breadcrumb.Item("Application"),
        ]
    )
