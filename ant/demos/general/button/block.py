from reflect_html import *
from reflect_antd import Button


def app():
    return [
        Button("Primary", type="primary", block=True),
        Button("Default", block=True),
        Button("Dashed", type="dashed", block=True),
        Button("Link", type="link", block=True),
    ]
