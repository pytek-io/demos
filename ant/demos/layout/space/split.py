from reflect_html import *
from reflect_antd import Space, Typography, Divider


def app():
    return Space(
        [Typography.Link("Link"), Typography.Link("Link"), Typography.Link("Link")],
        split=Divider(type="vertical"),
    )
