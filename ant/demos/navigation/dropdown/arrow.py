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
    return html.div(
        [
            antd.Dropdown(
                antd.Button("bottomLeft"),
                overlay=menu,
                placement="bottomLeft",
                arrow=True,
            ),
            antd.Dropdown(
                antd.Button("bottomCenter"),
                overlay=menu,
                placement="bottomCenter",
                arrow=True,
            ),
            antd.Dropdown(
                antd.Button("bottomRight"),
                overlay=menu,
                placement="bottomRight",
                arrow=True,
            ),
            html.br(),
            antd.Dropdown(
                antd.Button("topLeft"), overlay=menu, placement="topLeft", arrow=True
            ),
            antd.Dropdown(
                antd.Button("topCenter"),
                overlay=menu,
                placement="topCenter",
                arrow=True,
            ),
            antd.Dropdown(
                antd.Button("topRight"), overlay=menu, placement="topRight", arrow=True
            ),
        ]
    )
