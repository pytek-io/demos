import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

import reflect as r

Header, Content, Footer, Sider = (
    antd.Layout.Header,
    antd.Layout.Content,
    antd.Layout.Footer,
    antd.Layout.Sider,
)


def app():
    collapsed = r.ObservableValue(False)

    def onCollapse(collapsed_value):
        print(collapsed_value)
        collapsed.set(collapsed_value)

    return antd.Layout(
        [
            Sider(
                [
                    html.div(className="logo"),
                    antd.Menu(
                        items=[
                            {
                                "label": "Option 1",
                                "key": "1",
                                "icon": ant_icons.PieChartOutlined([]),
                            },
                            {
                                "label": "Option 2",
                                "key": "2",
                                "icon": ant_icons.DesktopOutlined([]),
                            },
                            {
                                "children": [
                                    {"label": "Tom", "key": "3"},
                                    {"label": "Bill", "key": "4"},
                                    {"label": "Alex", "key": "5"},
                                ],
                                "key": "sub1",
                                "icon": ant_icons.UserOutlined([]),
                                "label": "User",
                            },
                            {
                                "children": [
                                    {"label": "Team 1", "key": "6"},
                                    {"label": "Team 2", "key": "8"},
                                ],
                                "key": "sub2",
                                "icon": ant_icons.TeamOutlined([]),
                                "label": "Team",
                            },
                            {
                                "label": "Files",
                                "key": "9",
                                "icon": ant_icons.FileOutlined([]),
                            },
                        ],
                        theme="dark",
                        defaultSelectedKeys=["1"],
                        mode="inline",
                    ),
                ],
                collapsible=True,
                collapsed=collapsed,
                onCollapse=r.Callback(onCollapse),
            ),
            antd.Layout(
                [
                    Header(className="site-layout-background", style=dict(padding=0)),
                    Content(
                        [
                            antd.Breadcrumb(
                                [
                                    antd.Breadcrumb.Item("User"),
                                    antd.Breadcrumb.Item("Bill"),
                                ],
                                style=dict(margin="16px 0"),
                            ),
                            html.div(
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
