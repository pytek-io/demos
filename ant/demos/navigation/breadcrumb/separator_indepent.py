import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Breadcrumb(
        [
            antd.Breadcrumb.Item("Location"),
            antd.Breadcrumb.Separator(":"),
            antd.Breadcrumb.Item("Application Center", href=""),
            antd.Breadcrumb.Separator(),
            antd.Breadcrumb.Item("Application List", href=""),
            antd.Breadcrumb.Separator(),
            antd.Breadcrumb.Item("An Application"),
        ],
        separator="",
    )
