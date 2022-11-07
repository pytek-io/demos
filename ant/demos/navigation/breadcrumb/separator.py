import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Breadcrumb(
        [
            antd.Breadcrumb.Item("Home"),
            antd.Breadcrumb.Item("Application Center", href=""),
            antd.Breadcrumb.Item("Application List", href=""),
            antd.Breadcrumb.Item("An Application"),
        ],
        separator=">",
    )
