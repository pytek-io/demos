import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

SubMenu = antd.Menu.SubMenu


def app():
    switch_mode = antd.Switch("vertical mode", defaultChecked=False)
    switch_theme = antd.Switch("dark theme", defaultChecked=False)
    mode = lambda: "vertical" if switch_mode() else "inline"
    theme = lambda: "dark" if switch_theme() else "light"
    return html.div(
        [
            switch_mode,
            antd.Divider(type="vertical"),
            switch_theme,
            html.br(),
            html.br(),
            antd.Menu(
                [
                    antd.Menu.Item(
                        "Navigation One", key="1", icon=ant_icons.MailOutlined([])
                    ),
                    antd.Menu.Item(
                        "Navigation Two", key="2", icon=ant_icons.CalendarOutlined([])
                    ),
                    SubMenu(
                        [
                            antd.Menu.Item("Option 3", key="3"),
                            antd.Menu.Item("Option 4", key="4"),
                            SubMenu(
                                [
                                    antd.Menu.Item("Option 5", key="5"),
                                    antd.Menu.Item("Option 6", key="6"),
                                ],
                                key="sub1-2",
                                title="Submenu",
                            ),
                        ],
                        key="sub1",
                        icon=ant_icons.AppstoreOutlined([]),
                        title="Navigation Two",
                    ),
                    SubMenu(
                        [
                            antd.Menu.Item("Option 7", key="7"),
                            antd.Menu.Item("Option 8", key="8"),
                            antd.Menu.Item("Option 9", key="9"),
                            antd.Menu.Item("Option 10", key="10"),
                        ],
                        key="sub2",
                        icon=ant_icons.SettingOutlined([]),
                        title="Navigation Three",
                    ),
                    antd.Menu.Item(
                        html.a(
                            "Ant Design",
                            href="https://ant.design",
                            target="_blank",
                            rel="noopener noreferrer",
                        ),
                        key="link",
                        icon=ant_icons.LinkOutlined([]),
                    ),
                ],
                style=dict(width=256),
                defaultSelectedKeys=["1"],
                defaultOpenKeys=["sub1"],
                mode=mode,
                theme=theme,
            ),
        ]
    )
