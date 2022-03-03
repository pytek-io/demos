from reflect_html import *
from reflect_antd import Popover, Button

content = div([p("Content"), p("Content")])


def app():
    return div(
        [
            Popover(
                Button("Hover me"), content=content, title="Title", trigger="hover"
            ),
            Popover(
                Button("Focus me"), content=content, title="Title", trigger="focus"
            ),
            Popover(
                Button("Click me"), content=content, title="Title", trigger="click"
            ),
        ]
    )
