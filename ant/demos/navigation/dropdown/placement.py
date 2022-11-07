import reflect_antd as antd
import reflect_html as html

menu = antd.Menu(
    [
        antd.Menu.Item(
            html.a(
                "1st menu item",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.alipay.com/",
            )
        ),
        antd.Menu.Item(
            html.a(
                "2nd menu item",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.taobao.com/",
            )
        ),
        antd.Menu.Item(
            html.a(
                "3rd menu item",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.tmall.com/",
            )
        ),
    ]
)


def app():
    return antd.Space(
        [
            antd.Space(
                [
                    antd.Dropdown(
                        antd.Button("bottomLeft"), overlay=menu, placement="bottomLeft"
                    ),
                    antd.Dropdown(
                        antd.Button("bottomCenter"),
                        overlay=menu,
                        placement="bottomCenter",
                    ),
                    antd.Dropdown(
                        antd.Button("bottomRight"),
                        overlay=menu,
                        placement="bottomRight",
                    ),
                ],
                wrap=True,
            ),
            antd.Space(
                [
                    antd.Dropdown(
                        antd.Button("topLeft"), overlay=menu, placement="topLeft"
                    ),
                    antd.Dropdown(
                        antd.Button("topCenter"), overlay=menu, placement="topCenter"
                    ),
                    antd.Dropdown(
                        antd.Button("topRight"), overlay=menu, placement="topRight"
                    ),
                ],
                wrap=True,
            ),
        ],
        direction="vertical",
    )
