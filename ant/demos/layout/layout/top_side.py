from reflect_html import *
from reflect_antd import Layout, Menu, Breadcrumb
from reflect_ant_icons import (
    UserOutlined,
    LaptopOutlined,
    NotificationOutlined,
)

SubMenu = Menu.SubMenu
Header, Content, Footer, Sider = (
    Layout.Header,
    Layout.Content,
    Layout.Footer,
    Layout.Sider,
)


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
            Content(
                [
                    Breadcrumb(
                        [
                            Breadcrumb.Item("Home"),
                            Breadcrumb.Item("List"),
                            Breadcrumb.Item("App"),
                        ],
                        style=dict(margin="16px 0"),
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
                                    style=dict(height="100%"),
                                ),
                                className="site-layout-background",
                                width=200,
                            ),
                            Content(
                                "Content", style=dict(padding="0 24px", minHeight=280)
                            ),
                        ],
                        className="site-layout-background",
                        style=dict(padding="24px 0"),
                    ),
                ],
                style=dict(padding="0 50px"),
            ),
            Footer(
                "Ant Design ©2018 Created by Ant UED", style=dict(textAlign="center")
            ),
        ]
    )
