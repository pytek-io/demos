from reflect_html import *
from reflect_antd import Layout, Menu, Breadcrumb
from reflect_ant_icons import (
    UserOutlined,
    LaptopOutlined,
    NotificationOutlined,
)

SubMenu = Menu.SubMenu
Header, Content, Sider = Layout.Header, Layout.Content, Layout.Sider


def app():
    return Layout(
        [
            Header(
                [
                    div(className="logo"),
                    Menu(
                        [
                            Menu.Item("nav 1", key="1"),
                            Menu.Item("nav 2", key="2"),
                            Menu.Item("nav 3", key="3"),
                        ],
                        theme="dark",
                        mode="horizontal",
                        defaultSelectedKeys=["2"],
                    ),
                ],
                className="header",
            ),
            Layout(
                [
                    Sider(
                        Menu(
                            [
                                SubMenu(
                                    [
                                        Menu.Item("option1", key="1"),
                                        Menu.Item("option2", key="2"),
                                        Menu.Item("option3", key="3"),
                                        Menu.Item("option4", key="4"),
                                    ],
                                    key="sub1",
                                    icon=UserOutlined([]),
                                    title="subnav 1",
                                ),
                                SubMenu(
                                    [
                                        Menu.Item("option5", key="5"),
                                        Menu.Item("option6", key="6"),
                                        Menu.Item("option7", key="7"),
                                        Menu.Item("option8", key="8"),
                                    ],
                                    key="sub2",
                                    icon=LaptopOutlined([]),
                                    title="subnav 2",
                                ),
                                SubMenu(
                                    [
                                        Menu.Item("option9", key="9"),
                                        Menu.Item("option10", key="10"),
                                        Menu.Item("option11", key="11"),
                                        Menu.Item("option12", key="12"),
                                    ],
                                    key="sub3",
                                    icon=NotificationOutlined([]),
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
                    Layout(
                        [
                            Breadcrumb(
                                [
                                    Breadcrumb.Item("Home"),
                                    Breadcrumb.Item("List"),
                                    Breadcrumb.Item("App"),
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
