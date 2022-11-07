import reflect_antd as antd
import reflect_html as html

menu = antd.Menu(
    [
        antd.Menu.Item(
            html.a(
                "General",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.alipay.com/",
            )
        ),
        antd.Menu.Item(
            html.a(
                "Layout",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.taobao.com/",
            )
        ),
        antd.Menu.Item(
            html.a(
                "Navigation",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.tmall.com/",
            )
        ),
    ]
)


def app():
    return antd.Breadcrumb(
        [
            antd.Breadcrumb.Item("Ant Design"),
            antd.Breadcrumb.Item(html.a("Component", href="")),
            antd.Breadcrumb.Item(html.a("General", href=""), overlay=menu),
            antd.Breadcrumb.Item("Button"),
        ]
    )
