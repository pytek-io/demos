import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

SubMenu = antd.Menu.SubMenu
Header, Content, Sider = (antd.Layout.Header, antd.Layout.Content, antd.Layout.Sider)


def app():
    return antd.Layout(
        [
            Header(
                [
                    html.div(className="logo"),
                    antd.Menu(
                        [
                            antd.Menu.Item("nav 1", key="1"),
                            antd.Menu.Item("nav 2", key="2"),
                            antd.Menu.Item("nav 3", key="3"),
                        ],
                        theme="dark",
                        mode="horizontal",
                        defaultSelectedKeys=["2"],
                    ),
                ],
                className="header",
            ),
            antd.Layout(
                [
                    Sider(
                        antd.Menu(
                            [
                                SubMenu(
                                    [
                                        antd.Menu.Item("option1", key="1"),
                                        antd.Menu.Item("option2", key="2"),
                                        antd.Menu.Item("option3", key="3"),
                                        antd.Menu.Item("option4", key="4"),
                                    ],
                                    key="sub1",
                                    icon=ant_icons.UserOutlined([]),
                                    title="subnav 1",
                                ),
                                SubMenu(
                                    [
                                        antd.Menu.Item("option5", key="5"),
                                        antd.Menu.Item("option6", key="6"),
                                        antd.Menu.Item("option7", key="7"),
                                        antd.Menu.Item("option8", key="8"),
                                    ],
                                    key="sub2",
                                    icon=ant_icons.LaptopOutlined([]),
                                    title="subnav 2",
                                ),
                                SubMenu(
                                    [
                                        antd.Menu.Item("option9", key="9"),
                                        antd.Menu.Item("option10", key="10"),
                                        antd.Menu.Item("option11", key="11"),
                                        antd.Menu.Item("option12", key="12"),
                                    ],
                                    key="sub3",
                                    icon=ant_icons.NotificationOutlined([]),
                                    title="subnav 3",
                                ),
                            ],
                            mode="inline",
                            defaultSelectedKeys=["1"],
                            defaultOpenKeys=["sub1"],
                            style=dict(height="100%", borderRight=0),
                        ),
                        width=200,
                        className="site-layout-background",
                    ),
                    antd.Layout(
                        [
                            antd.Breadcrumb(
                                [
                                    antd.Breadcrumb.Item("Home"),
                                    antd.Breadcrumb.Item("List"),
                                    antd.Breadcrumb.Item("App"),
                                ],
                                style=dict(margin="16px 0"),
                            ),
                            Content(
                                "Content",
                                className="site-layout-background",
                                style=dict(padding=24, margin=0, minHeight=280),
                            ),
                        ],
                        style=dict(padding="0 24px 24px"),
                    ),
                ]
            ),
        ]
    )
