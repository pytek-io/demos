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
                        items=[
                            {"label": "nav 1", "key": "1"},
                            {"label": "nav 2", "key": "2"},
                            {"label": "nav 3", "key": "3"},
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
                        style={"margin": "16px 0"},
                    ),
                    html.div("Content", className="site-layout-content"),
                ],
                style={"padding": "0 50px"},
            ),
            Footer(
                "Ant Design ©2018 Created by Ant UED", style={"textAlign": "center"}
            ),
        ],
        className="layout",
    )
