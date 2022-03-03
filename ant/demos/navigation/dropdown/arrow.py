from reflect_html import *
from reflect_antd import Menu, Dropdown, Button

menu = Menu(
    [
        Menu.Item(
            a(
                "1st menu item",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.alipay.com/",
            )
        ),
        Menu.Item(
            a(
                "2nd menu item",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.taobao.com/",
            )
        ),
        Menu.Item(
            a(
                "3rd menu item",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.tmall.com/",
            )
        ),
    ]
)


def app():
    return [
        Dropdown(
            Button("bottomLeft"), overlay=menu, placement="bottomLeft", arrow=True
        ),
        Dropdown(
            Button("bottomCenter"), overlay=menu, placement="bottomCenter", arrow=True
        ),
        Dropdown(
            Button("bottomRight"), overlay=menu, placement="bottomRight", arrow=True
        ),
        br(),
        Dropdown(Button("topLeft"), overlay=menu, placement="topLeft", arrow=True),
        Dropdown(Button("topCenter"), overlay=menu, placement="topCenter", arrow=True),
        Dropdown(Button("topRight"), overlay=menu, placement="topRight", arrow=True),
    ]
