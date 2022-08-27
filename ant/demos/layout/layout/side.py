from reflect_html import *
from reflect_antd import Layout, Menu, Breadcrumb
from reflect_ant_icons import (
    PieChartOutlined,
    DesktopOutlined,
    UserOutlined,
    TeamOutlined,
    FileOutlined,
)
from reflect import Callback
from reflect import create_observable

Header, Content, Footer, Sider = (
    Layout.Header,
    Layout.Content,
    Layout.Footer,
    Layout.Sider,
)
SubMenu = Menu.SubMenu


def app():
    collapsed = create_observable(False)

    def onCollapse(collapsed_value):
        print(collapsed_value)
        collapsed.set(collapsed_value)

    return Layout(
        [
            Sider(
                [
                    div(className="logo"),
                    Menu(
                        [
                            Menu.Item("Option 1", key="1", icon=PieChartOutlined([])),
                            Menu.Item("Option 2", key="2", icon=DesktopOutlined([])),
                            SubMenu(
                                [
                                    Menu.Item("Tom", key="3"),
                                    Menu.Item("Bill", key="4"),
                                    Menu.Item("Alex", key="5"),
                                ],
                                key="sub1",
                                icon=UserOutlined([]),
                                title="User",
                            ),
                            SubMenu(
                                [
                                    Menu.Item("Team 1", key="6"),
                                    Menu.Item("Team 2", key="8"),
                                ],
                                key="sub2",
                                icon=TeamOutlined([]),
                                title="Team",
                            ),
                            Menu.Item("Files", key="9", icon=FileOutlined([])),
                        ],
                        theme="dark",
                        defaultSelectedKeys=["1"],
                        mode="inline",
                    ),
                ],
                collapsible=True,
                collapsed=collapsed,
                onCollapse=Callback(onCollapse),
            ),
            Layout(
                [
                    Header(className="site-layout-background", style=dict(padding=0)),
                    Content(
                        [
                            Breadcrumb(
                                [Breadcrumb.Item("User"), Breadcrumb.Item("Bill")],
                                style=dict(margin="16px 0"),
                            ),
                            div(
                                "Bill is a cat.",
                                className="site-layout-background",
                                style=dict(padding=24, minHeight=360),
                            ),
                        ],
                        style=dict(margin="0 16px"),
                    ),
                    Footer(
                        "Ant Design ©2018 Created by Ant UED",
                        style=dict(textAlign="center"),
                    ),
                ],
                className="site-layout",
            ),
        ],
        style=dict(minHeight="100vh"),
    )
