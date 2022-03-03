from reflect_html import *
from reflect_antd import Breadcrumb, Menu

menu = Menu(
    [
        Menu.Item(
            a(
                "General",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.alipay.com/",
            )
        ),
        Menu.Item(
            a(
                "Layout",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.taobao.com/",
            )
        ),
        Menu.Item(
            a(
                "Navigation",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.tmall.com/",
            )
        ),
    ]
)


def app():
    return Breadcrumb(
        [
            Breadcrumb.Item("Ant Design"),
            Breadcrumb.Item(a("Component", href="")),
            Breadcrumb.Item(a("General", href=""), overlay=menu),
            Breadcrumb.Item("Button"),
        ]
    )
