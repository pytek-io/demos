from reflect_html import *
from reflect_antd import Tag
from reflect_ant_icons import CloseCircleOutlined


def app():
    return div(
        [
            Tag("Tag1", closable=True, closeIcon="关 闭"),
            Tag("Tag2", closable=True, closeIcon=CloseCircleOutlined([])),
        ]
    )
