import render_antd as antd
import render_html as html

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
                antd.Button("bottom"),
                menu={"items": items},
                placement="bottom",
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
                antd.Button("top"), menu={"items": items}, placement="top", arrow=True
            ),
            antd.Dropdown(
                antd.Button("topRight"),
                menu={"items": items},
                placement="topRight",
                arrow=True,
            ),
        ]
    )
