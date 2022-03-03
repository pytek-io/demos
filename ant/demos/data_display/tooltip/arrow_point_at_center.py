from reflect_html import *
from reflect_antd import Tooltip, Button


def app():
    return div(
        [
            Tooltip(
                Button("Align edge / 边缘对齐"), placement="topLeft", title="Prompt Text"
            ),
            Tooltip(
                Button("Arrow points to center / 箭头指向中心"),
                placement="topLeft",
                title="Prompt Text",
                arrowPointAtCenter=True,
            ),
        ]
    )
