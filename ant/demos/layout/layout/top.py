import render_antd as antd
import render_html as html

Header, Content, Footer = (antd.Layout.Header, antd.Layout.Content, antd.Layout.Footer)


def app(_):
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
                        items=[{"title": "Home"}, {"title": "List"}, {"title": "App"}],
                    ),
                    html.div("Content", className="site-layout-content"),
                ],
            ),
            Footer(
                "Ant Design ©2018 Created by Ant UED", style={"textAlign": "center"}
            ),
        ],
        className="layout",
    )
