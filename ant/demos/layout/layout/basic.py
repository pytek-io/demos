from reflect_antd import Layout
from reflect_html import div

Header, Footer, Sider, Content = (
    Layout.Header,
    Layout.Footer,
    Layout.Sider,
    Layout.Content,
)


def app():
    return div(
        [
            Layout([Header("Header"), Content("Content"), Footer("Footer")]),
            Layout(
                [
                    Header("Header"),
                    Layout([Sider("Sider"), Content("Content")]),
                    Footer("Footer"),
                ]
            ),
            Layout(
                [
                    Header("Header"),
                    Layout([Content("Content"), Sider("Sider")]),
                    Footer("Footer"),
                ]
            ),
            Layout(
                [
                    Sider("Sider"),
                    Layout([Header("Header"), Content("Content"), Footer("Footer")]),
                ]
            ),
        ]
    )
