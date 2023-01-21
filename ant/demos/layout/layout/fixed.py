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
                ],
                style={"position": "fixed", "zIndex": 1, "width": "100%"},
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
                    html.div(
                        "Content",
                        className="site-layout-background",
                        style={"padding": 24, "minHeight": 380},
                    ),
                ],
                className="site-layout",
                style={"padding": "0 50px", "marginTop": 64},
            ),
            Footer(
                "Ant Design ©2018 Created by Ant UED", style={"textAlign": "center"}
            ),
        ]
    )
