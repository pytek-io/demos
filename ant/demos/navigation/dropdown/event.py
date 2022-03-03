from reflect_html import *
from reflect_antd import Menu, Dropdown, message
from reflect_ant_icons import DownOutlined
from reflect import Callback


def onClick(key):
    message.info(f"Click on item {key}")


def app():

    menu = Menu(
        [
            Menu.Item("1st menu item", key="1"),
            Menu.Item("2nd menu item", key="2"),
            Menu.Item("3rd menu item", key="3"),
        ],
        onClick=Callback(onClick, "key"),
    )
    return [
        Dropdown(
            a(
                ["Hover me, Click menu item", DownOutlined()],
                className="ant-dropdown-link",
                onClick=lambda e: e.preventDefault(),
            ),
            overlay=menu,
        ),
    ]
