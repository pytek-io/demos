from reflect_html import *
from reflect_antd import Button, Tooltip
from reflect_ant_icons import SearchOutlined


def app():
    return [
        Tooltip(
            Button(type="primary", shape="circle", icon=SearchOutlined([])),
            title="search",
        ),
        Button("A", type="primary", shape="circle"),
        Button("Search", type="primary", icon=SearchOutlined([])),
        Tooltip(Button(shape="circle", icon=SearchOutlined([])), title="search"),
        Button("Search", icon=SearchOutlined([])),
        br(),
        Tooltip(Button(shape="circle", icon=SearchOutlined([])), title="search"),
        Button("Search", icon=SearchOutlined([])),
        Tooltip(
            Button(type="dashed", shape="circle", icon=SearchOutlined([])),
            title="search",
        ),
        Button("Search", type="dashed", icon=SearchOutlined([])),
    ]
