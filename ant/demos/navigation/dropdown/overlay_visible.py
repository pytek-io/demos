from reflect_html import *
from reflect_antd import Menu, Dropdown
from reflect_ant_icons import DownOutlined
from reflect import make_observable
from reflect import Callback


def app():
    raise NotImplementedError()
    visible = make_observable(False)

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
