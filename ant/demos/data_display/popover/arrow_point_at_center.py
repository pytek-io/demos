from reflect_html import *
from reflect_antd import Popover, Button



def app():
    content = div([p("Content"), p("Content")])
    text = span("Title")
    return div(
        [
            Popover(
                Button("Align edge"),
                placement="topLeft",
                title=text,
                content=content,
            ),
            Popover(
                Button("Arrow points to center"),
                placement="topLeft",
                title=text,
                content=content,
                arrowPointAtCenter=True,
            ),
        ]
    )
