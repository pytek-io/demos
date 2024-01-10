import render_antd as antd
import render_html as html


def app(_):
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
