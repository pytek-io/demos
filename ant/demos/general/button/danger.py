from reflect_html import *
from reflect_antd import Button


def app():
    return [
        Button("Primary", type="primary", danger=True),
        Button("Default", danger=True),
        Button("Dashed", type="dashed", danger=True),
        Button("Text", type="text", danger=True),
        Button("Link", type="link", danger=True),
    ]
