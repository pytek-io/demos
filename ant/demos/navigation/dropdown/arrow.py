import reflect_antd as antd
import reflect_html as html


items = [
    {
        "label": html.a(
            "1st menu item",
            target="_blank",
            rel="noopener noreferrer",
            href="http://www.alipay.com/",
        )
    },
    {
        "label": html.a(
            "2nd menu item",
            target="_blank",
            rel="noopener noreferrer",
            href="http://www.taobao.com/",
        )
    },
    {
        "label": html.a(
            "3rd menu item",
            target="_blank",
            rel="noopener noreferrer",
            href="http://www.tmall.com/",
        )
    },
]


def app():
    return html.div(
        [
            antd.Dropdown(
                antd.Button("bottomLeft"),
                menu={"items": items},
                placement="bottomLeft",
                arrow=True,
            ),
            antd.Dropdown(
                antd.Button("bottomCenter"),
                menu={"items": items},
                placement="bottomCenter",
                arrow=True,
            ),
            antd.Dropdown(
                antd.Button("bottomRight"),
                menu={"items": items},
                placement="bottomRight",
                arrow=True,
            ),
            html.br(),
            antd.Dropdown(
                antd.Button("topLeft"),
                menu={"items": items},
                placement="topLeft",
                arrow=True,
            ),
            antd.Dropdown(
                antd.Button("topCenter"),
                menu={"items": items},
                placement="topCenter",
                arrow=True,
            ),
            antd.Dropdown(
                antd.Button("topRight"),
                menu={"items": items},
                placement="topRight",
                arrow=True,
            ),
        ]
    )
