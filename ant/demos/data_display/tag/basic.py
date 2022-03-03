from reflect_html import *
from reflect_antd import Tag


def app():
    return [
        Tag("Tag 1"),
        Tag(a("Link", href="https://github.com/ant-design/ant-design/issues/1862")),
        Tag("Tag 2", closable=True, onClose=log),
        Tag("Prevent Default", closable=True, onClose=preventDefault),
    ]
