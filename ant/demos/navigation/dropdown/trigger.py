from reflect_html import *
from reflect_antd import Menu, Dropdown
from reflect_ant_icons import DownOutlined
from reflect import Callback

menu = Menu(
    [
        Menu.Item(a("1st menu item", href="http://www.google.com/"), key="0"),
        Menu.Item(a("2nd menu item", href="http://www.google.com/"), key="1"),
        Menu.Divider(),
        Menu.Item("3rd menu item", key="3"),
    ]
)


def app():
    return Dropdown(
        a(
            ["Click me", DownOutlined()],
            className="ant-dropdown-link",
            onClick=Callback(None, prevent_default=True),
        ),
        overlay=menu,
        trigger=["click"],
    )
