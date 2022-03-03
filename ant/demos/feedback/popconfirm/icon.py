from reflect_html import *
from reflect_antd import Popconfirm
from reflect_ant_icons import QuestionCircleOutlined


def app():
    return Popconfirm(
        a("Delete", href="#"),
        title="Are you sure？",
        icon=QuestionCircleOutlined(style={"color": "red"}),
    )
