from render import Callback, create_observable
from render_ant_icons import DownOutlined
from render_antd import Dropdown, Menu
from render_html import *


def app():
    raise NotImplementedError()
    visible = create_observable(False)

    def handleMenuClick(key):
        if key == "3":
            visible.set(False)

    def handleVisibleChange(value):
        print(value)
        visible.set(value)

    menu = Menu(
        [
            Menu.Item("Clicking me will not close the menu.", key="1"),
            Menu.Item("Clicking me will not close the menu also.", key="2"),
            Menu.Item("Clicking me will close the menu.", key="3"),
        ],
        onClick=[Callback(handleMenuClick), "key"],
    )

    return [
        Dropdown(
            a(
                ["Hover me", DownOutlined()],
                className="ant-dropdown-link",
                onClick=Callback(lambda e: e.preventDefault()),
            ),
            overlay=menu,
            onVisibleChange=Callback(handleVisibleChange),
            visible=visible,
        ),
    ]
