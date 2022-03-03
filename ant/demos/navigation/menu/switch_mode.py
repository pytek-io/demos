from reflect_html import *
from reflect_antd import Menu, Switch, Divider
from reflect_ant_icons import (
    CalendarOutlined,
    LinkOutlined,
    AppstoreOutlined,
    MailOutlined,
    SettingOutlined,
)

SubMenu = Menu.SubMenu


def app():
    switch_mode = Switch("vertical mode", defaultChecked=False)
    switch_theme = Switch("dark theme", defaultChecked=False)
    mode = lambda: "vertical" if switch_mode() else "inline"
    theme = lambda: "dark" if switch_theme() else "light"
    return [
        switch_mode,
        Divider(type="vertical"),
        switch_theme,
        br(),
        br(),
        Menu(
            [
                Menu.Item("Navigation One", key="1", icon=MailOutlined([])),
                Menu.Item("Navigation Two", key="2", icon=CalendarOutlined([])),
                SubMenu(
                    [
                        Menu.Item("Option 3", key="3"),
                        Menu.Item("Option 4", key="4"),
                        SubMenu(
                            [
                                Menu.Item("Option 5", key="5"),
                                Menu.Item("Option 6", key="6"),
                            ],
                            key="sub1-2",
                            title="Submenu",
                        ),
                    ],
                    key="sub1",
                    icon=AppstoreOutlined([]),
                    title="Navigation Two",
                ),
                SubMenu(
                    [
                        Menu.Item("Option 7", key="7"),
                        Menu.Item("Option 8", key="8"),
                        Menu.Item("Option 9", key="9"),
                        Menu.Item("Option 10", key="10"),
                    ],
                    key="sub2",
                    icon=SettingOutlined([]),
                    title="Navigation Three",
                ),
                Menu.Item(
                    a(
                        "Ant Design",
                        href="https://ant.design",
                        target="_blank",
                        rel="noopener noreferrer",
                    ),
                    key="link",
                    icon=LinkOutlined([]),
                ),
            ],
            style=dict(width=256),
            defaultSelectedKeys=["1"],
            defaultOpenKeys=["sub1"],
            mode=mode,
            theme=theme,
        ),
    ]
