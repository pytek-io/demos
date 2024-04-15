import render_antd as antd
import render_html as html

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


def app(_):
    return antd.Breadcrumb(
        items=[
            {"title": "Ant Design"},
            {"label": html.a("Component", href="")},
            {"title": html.a("General", href="")},
            {"title": "Button"},
        ],
    )
