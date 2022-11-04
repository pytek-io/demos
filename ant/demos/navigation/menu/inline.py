from reflect_html import *
from reflect_antd import Menu
from reflect_ant_icons import AppstoreOutlined, MailOutlined, SettingOutlined
from reflect import Callback

SubMenu = Menu.SubMenu


def app():
    return Menu(
        [
            SubMenu(
                [
                    Menu.ItemGroup(
                        [
                            Menu.Item("Option 1", key="1"),
                            Menu.Item("Option 2", key="2"),
                        ],
                        key="g1",
                        title="Item 1",
                    ),
                    Menu.ItemGroup(
                        [
                            Menu.Item("Option 3", key="3"),
                            Menu.Item("Option 4", key="4"),
                        ],
                        key="g2",
                        title="Item 2",
                    ),
                ],
                key="sub1",
                icon=MailOutlined([]),
                title="Navigation One",
            ),
            SubMenu(
                [
                    Menu.Item("Option 5", key="5"),
                    Menu.Item("Option 6", key="6"),
                    SubMenu(
                        [
                            Menu.Item("Option 7", key="7"),
                            Menu.Item("Option 8", key="8"),
                        ],
                        key="sub3",
                        title="Submenu",
                    ),
                ],
                key="sub2",
                icon=AppstoreOutlined([]),
                title="Navigation Two",
            ),
            SubMenu(
                [
                    Menu.Item("Option 9", key="9"),
                    Menu.Item("Option 10", key="10"),
                    Menu.Item("Option 11", key="11"),
                    Menu.Item("Option 12", key="12"),
                ],
                key="sub4",
                icon=SettingOutlined([]),
                title="Navigation Three",
            ),
        ],
        onClick=Callback(lambda key: print(f"clicked option {key}"), args="key"),
        style=dict(width=256),
        defaultSelectedKeys=["1"],
        defaultOpenKeys=["sub1"],
        mode="inline",
    )
