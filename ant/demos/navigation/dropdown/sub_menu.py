from reflect_html import *
from reflect_antd import Menu, Dropdown
from reflect_ant_icons import DownOutlined

SubMenu = Menu.SubMenu
menu = Menu(
    [
        Menu.ItemGroup(
            [Menu.Item("1st menu item"), Menu.Item("2nd menu item")],
            title="Group title",
        ),
        SubMenu(
            [Menu.Item("3rd menu item"), Menu.Item("4th menu item")], title="sub menu"
        ),
        SubMenu(
            [Menu.Item("5d menu item"), Menu.Item("6th menu item")],
            title="disabled sub menu",
            disabled=True,
        ),
    ]
)


def app():
    return Dropdown(
        a(
            ["Cascading menu", DownOutlined()],
            className="ant-dropdown-link",
            onClick=lambda e: e.preventDefault(),
        ),
        overlay=menu,
    )
