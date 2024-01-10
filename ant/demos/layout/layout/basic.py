import render_antd as antd
import render_html as html

Header, Footer, Sider, Content = (
    antd.Layout.Header,
    antd.Layout.Footer,
    antd.Layout.Sider,
    antd.Layout.Content,
)


def app(_):
    return html.div(
        [
            antd.Layout([Header("Header"), Content("Content"), Footer("Footer")]),
            antd.Layout(
                [
                    Header("Header"),
                    antd.Layout([Sider("Sider"), Content("Content")]),
                    Footer("Footer"),
                ]
            ),
            antd.Layout(
                [
                    Header("Header"),
                    antd.Layout([Content("Content"), Sider("Sider")]),
                    Footer("Footer"),
                ]
            ),
            antd.Layout(
                [
                    Sider("Sider"),
                    antd.Layout(
                        [Header("Header"), Content("Content"), Footer("Footer")]
                    ),
                ]
            ),
        ]
    )
