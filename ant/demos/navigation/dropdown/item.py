import reflect_ant_icons as ant_icons
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
            ),
            key="0",
        ),
        antd.Menu.Item(
            html.a(
                "2nd menu item",
                target="_blank",
                rel="noopener noreferrer",
                href="http://www.taobao.com/",
            ),
            key="1",
        ),
        antd.Menu.Divider(),
        antd.Menu.Item("3rd menu item（disabled）", key="3", disabled=True),
    ]
)


def app():
    return antd.Dropdown(
        html.a(
            ["Hover me", ant_icons.DownOutlined()],
            className="ant-dropdown-link",
            onClick=lambda e: e.preventDefault(),
        ),
        overlay=menu,
    )
