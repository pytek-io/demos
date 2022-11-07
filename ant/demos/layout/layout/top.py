import reflect_antd as antd
import reflect_html as html

Header, Content, Footer = (antd.Layout.Header, antd.Layout.Content, antd.Layout.Footer)


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
                ]
            ),
            Content(
                [
                    antd.Breadcrumb(
                        [
                            antd.Breadcrumb.Item("Home"),
                            antd.Breadcrumb.Item("List"),
                            antd.Breadcrumb.Item("App"),
                        ],
                        style=dict(margin="16px 0"),
                    ),
                    html.div("Content", className="site-layout-content"),
                ],
                style=dict(padding="0 50px"),
            ),
            Footer(
                "Ant Design ©2018 Created by Ant UED", style=dict(textAlign="center")
            ),
        ],
        className="layout",
    )
