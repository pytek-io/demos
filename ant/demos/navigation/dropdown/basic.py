import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html

items = [
    {
        "label": html.a(
            "1st menu item",
            target="_blank",
            rel="noopener noreferrer",
            href="http://www.google.com/",
        )
    },
    {
        "label": html.a(
            "2nd menu item",
            target="_blank",
            rel="noopener noreferrer",
            href="http://www.google.com/",
        )
    },
    {
        "label": html.a(
            "3rd menu item",
            target="_blank",
            rel="noopener noreferrer",
            href="http://www.google.com/",
        )
    },
    {"label": "a danger item", "danger": True},
]


def app(_):
    return antd.Dropdown(
        html.a(
            ["Hover me", ant_icons.DownOutlined()],
            className="ant-dropdown-link",
            onClick=r.Callback(prevent_default=True),
        ),
        menu={"items": items},
    )
