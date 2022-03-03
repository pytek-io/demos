from reflect_html import *
from reflect_antd import Layout, Menu, Breadcrumb

Header, Content, Footer = Layout.Header, Layout.Content, Layout.Footer


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
                style=dict(position="fixed", zIndex=1, width="100%"),
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
                    div(
                        "Content",
                        className="site-layout-background",
                        style=dict(padding=24, minHeight=380),
                    ),
                ],
                className="site-layout",
                style=dict(padding="0 50px", marginTop=64),
            ),
            Footer(
                "Ant Design ©2018 Created by Ant UED", style=dict(textAlign="center")
            ),
        ]
    )
