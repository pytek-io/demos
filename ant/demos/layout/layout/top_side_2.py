import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html

Header, Content, Sider = (antd.Layout.Header, antd.Layout.Content, antd.Layout.Sider)


def app():
    return antd.Layout(
        [
            Header(
                [
                    html.div(className="logo"),
                    antd.Menu(
                        items=[
                            {"label": "nav 1", "key": "1"},
                            {"label": "nav 2", "key": "2"},
                            {"label": "nav 3", "key": "3"},
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
                            items=[
                                {
                                    "children": [
                                        {"label": "option1", "key": "1"},
                                        {"label": "option2", "key": "2"},
                                        {"label": "option3", "key": "3"},
                                        {"label": "option4", "key": "4"},
                                    ],
                                    "key": "sub1",
                                    "icon": ant_icons.UserOutlined([]),
                                    "label": "subnav 1",
                                },
                                {
                                    "children": [
                                        {"label": "option5", "key": "5"},
                                        {"label": "option6", "key": "6"},
                                        {"label": "option7", "key": "7"},
                                        {"label": "option8", "key": "8"},
                                    ],
                                    "key": "sub2",
                                    "icon": ant_icons.LaptopOutlined([]),
                                    "label": "subnav 2",
                                },
                                {
                                    "children": [
                                        {"label": "option9", "key": "9"},
                                        {"label": "option10", "key": "10"},
                                        {"label": "option11", "key": "11"},
                                        {"label": "option12", "key": "12"},
                                    ],
                                    "key": "sub3",
                                    "icon": ant_icons.NotificationOutlined([]),
                                    "label": "subnav 3",
                                },
                            ],
                            mode="inline",
                            defaultSelectedKeys=["1"],
                            defaultOpenKeys=["sub1"],
                            style={"height": "100%", "borderRight": 0},
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
                                style={"margin": "16px 0"},
                            ),
                            Content(
                                "Content",
                                className="site-layout-background",
                                style={"padding": 24, "margin": 0, "minHeight": 280},
                            ),
                        ],
                        style={"padding": "0 24px 24px"},
                    ),
                ]
            ),
        ]
    )
