import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html

items = [
    {
        "label": html.a(
            "1st menu item",
            target="_blank",
            rel="noopener noreferrer",
            href="http://www.alipay.com/",
        ),
        "key": "0",
    },
    {
        "label": html.a(
            "2nd menu item",
            target="_blank",
            rel="noopener noreferrer",
            href="http://www.taobao.com/",
        ),
        "key": "1",
    },
    {"type": "group"},
    {"label": "3rd menu item（disabled）", "key": "3", "disabled": True},
]


def app():
    return antd.Dropdown(
        html.a(
            ["Hover me", ant_icons.DownOutlined()],
            className="ant-dropdown-link",
            onClick=lambda e: e.preventDefault(),
        ),
        menu={"items": items},
    )
