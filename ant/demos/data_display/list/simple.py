from reflect_html import *
from reflect_antd import List, Divider
from reflect import js

data = [
    'Magna officia mollit commodo occaecat esse id.',
    "Ea nostrud aliqua duis tempor duis in dolor.",
    "Pariatur reprehenderit enim nulla sit ex adipiscing.",
    "Excepteur velit pariatur ad dolore ipsum ea.",
]


def app():
    return div([
        Divider("Default Size", orientation="left"),
        List(
            header=div("Header"),
            footer=div("Footer"),
            bordered=True,
            dataSource=data,
            renderItem=js("simple_list_renderer_1"),
        ),
        Divider("Small Size", orientation="left"),
        List(
            size="small",
            header=div("Header"),
            footer=div("Footer"),
            bordered=True,
            dataSource=data,
            renderItem=js("simple_list_renderer_2"),
        ),
        Divider("Large Size", orientation="left"),
        List(
            size="large",
            header=div("Header"),
            footer=div("Footer"),
            bordered=True,
            dataSource=data,
            renderItem=js("simple_list_renderer_2"),
        ),
    ]
)