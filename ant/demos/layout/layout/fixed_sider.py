import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

Header, Content, Footer, Sider = (
    antd.Layout.Header,
    antd.Layout.Content,
    antd.Layout.Footer,
    antd.Layout.Sider,
)


def app():
    return antd.Layout(
        [
            Sider(
                [
                    html.div(className="logo"),
                    antd.Menu(
                        [
                            antd.Menu.Item(
                                "nav 1", key="1", icon=ant_icons.UserOutlined([])
                            ),
                            antd.Menu.Item(
                                "nav 2", key="2", icon=ant_icons.VideoCameraOutlined([])
                            ),
                            antd.Menu.Item(
                                "nav 3", key="3", icon=ant_icons.UploadOutlined([])
                            ),
                            antd.Menu.Item(
                                "nav 4", key="4", icon=ant_icons.BarChartOutlined([])
                            ),
                            antd.Menu.Item(
                                "nav 5", key="5", icon=ant_icons.CloudOutlined([])
                            ),
                            antd.Menu.Item(
                                "nav 6", key="6", icon=ant_icons.AppstoreOutlined([])
                            ),
                            antd.Menu.Item(
                                "nav 7", key="7", icon=ant_icons.TeamOutlined([])
                            ),
                            antd.Menu.Item(
                                "nav 8", key="8", icon=ant_icons.ShopOutlined([])
                            ),
                        ],
                        theme="dark",
                        mode="inline",
                        defaultSelectedKeys=["4"],
                    ),
                ],
                style=dict(overflow="auto", height="100vh", position="fixed", left=0),
            ),
            antd.Layout(
                [
                    Header(className="site-layout-background", style=dict(padding=0)),
                    Content(
                        html.div(
                            [
                                "...",
                                html.br(),
                                "Really",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "long",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "...",
                                html.br(),
                                "content",
                            ],
                            className="site-layout-background",
                            style=dict(padding=24, textAlign="center"),
                        ),
                        style=dict(margin="24px 16px 0", overflow="initial"),
                    ),
                    Footer(
                        "Ant Design ©2018 Created by Ant UED",
                        style=dict(textAlign="center"),
                    ),
                ],
                className="site-layout",
                style=dict(marginLeft=200),
            ),
        ]
    )
