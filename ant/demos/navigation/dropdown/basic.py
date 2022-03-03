from reflect_html import *
from reflect_antd import Menu, Dropdown
from reflect_ant_icons import DownOutlined

menu = Menu(
    [
        Menu.Item(
            a(
                "1st menu item",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.google.com/",
            )
        ),
        Menu.Item(
            a(
                "2nd menu item",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.google.com/",
            )
        ),
        Menu.Item(
            a(
                "3rd menu item",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.google.com/",
            )
        ),
        Menu.Item("a danger item", danger=True),
    ]
)


def app():
    return Dropdown(
        a(
            ["Hover me", DownOutlined()],
            className="ant-dropdown-link",
            onClick=lambda e: e.preventDefault(),
        ),
        overlay=menu,
    )
