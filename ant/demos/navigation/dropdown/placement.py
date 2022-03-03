from reflect_html import *
from reflect_antd import Menu, Dropdown, Button, Space

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
    return Space(
        [
            Space(
                [
                    Dropdown(
                        Button("bottomLeft"), overlay=menu, placement="bottomLeft"
                    ),
                    Dropdown(
                        Button("bottomCenter"), overlay=menu, placement="bottomCenter"
                    ),
                    Dropdown(
                        Button("bottomRight"), overlay=menu, placement="bottomRight"
                    ),
                ],
                wrap=True,
            ),
            Space(
                [
                    Dropdown(Button("topLeft"), overlay=menu, placement="topLeft"),
                    Dropdown(Button("topCenter"), overlay=menu, placement="topCenter"),
                    Dropdown(Button("topRight"), overlay=menu, placement="topRight"),
                ],
                wrap=True,
            ),
        ],
        direction="vertical",
    )
