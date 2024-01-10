import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html

items = [
    {"label": html.a("1st menu item", href="http://www.google.com/"), "key": "0"},
    {"label": html.a("2nd menu item", href="http://www.google.com/"), "key": "1"},
    {"type": "group"},
    {"label": "3rd menu item", "key": "3"},
]


def app(_):
    return antd.Dropdown(
        html.a(
            ["Click me", ant_icons.DownOutlined()],
            className="ant-dropdown-link",
            onClick=r.Callback(None, prevent_default=True),
        ),
        menu={"items": items},
        trigger=["click"],
    )
