from reflect_html import *
from reflect_antd import Button, Menu, Dropdown
from reflect import Callback


def handle_menu_click(key):
    print("click", key)


def app():
    def build_menu():
        return [
            Menu.Item("1st item", key="1"),
            Menu.Item("2nd item", key="2"),
            Menu.Item("3rd item", key="3"),
        ]

    menu = Menu(
        build_menu, 
        onClick=Callback(handle_menu_click, "key")
    )
    menu1 = Menu(
        [
            Menu.Item("1st item", key="1"),
            Menu.Item("2nd item", key="2"),
            Menu.Item("3rd item", key="3"),
        ],
        onClick=Callback(handle_menu_click, "key"),
    )
    # print("FIXME, passing a method badly crash everything")
    return [
        Button("primary", type="primary"),
        Button("secondary"),
        # build_menu,
        Dropdown.Button("Actions", overlay=menu),
    ]
