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


def app(_):
    return antd.Space(
        [
            antd.Space(
                [
                    antd.Dropdown(
                        antd.Button("bottomLeft"),
                        menu={"items": items},
                        placement="bottomLeft",
                    ),
                    antd.Dropdown(
                        antd.Button("bottomCenter"),
                        menu={"items": items},
                        placement="bottomCenter",
                    ),
                    antd.Dropdown(
                        antd.Button("bottomRight"),
                        menu={"items": items},
                        placement="bottomRight",
                    ),
                ],
                wrap=True,
            ),
            antd.Space(
                [
                    antd.Dropdown(
                        antd.Button("topLeft"),
                        menu={"items": items},
                        placement="topLeft",
                    ),
                    antd.Dropdown(
                        antd.Button("topCenter"),
                        menu={"items": items},
                        placement="topCenter",
                    ),
                    antd.Dropdown(
                        antd.Button("topRight"),
                        menu={"items": items},
                        placement="topRight",
                    ),
                ],
                wrap=True,
            ),
        ],
        direction="vertical",
    )
