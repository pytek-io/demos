import reflect_antd as antd
import reflect_html as html

items = [
    {
        "label": html.a(
            "General",
            target="_blank",
            rel="noopener noreferrer",
            href="http://www.alipay.com/",
        )
    },
    {
        "label": html.a(
            "Layout",
            target="_blank",
            rel="noopener noreferrer",
            href="http://www.taobao.com/",
        )
    },
    {
        "label": html.a(
            "Navigation",
            target="_blank",
            rel="noopener noreferrer",
            href="http://www.tmall.com/",
        )
    },
]


def app():
    return antd.Breadcrumb(
        [
            antd.Breadcrumb.Item("Ant Design"),
            antd.Breadcrumb.Item(html.a("Component", href="")),
            antd.Breadcrumb.Item(html.a("General", href=""), menu={"items": items}),
            antd.Breadcrumb.Item("Button"),
        ]
    )
