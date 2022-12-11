import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

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


def app():
    return antd.Dropdown(
        html.a(
            ["Hover me", ant_icons.DownOutlined()],
            className="ant-dropdown-link",
            onClick=lambda e: e.preventDefault(),
        ),
        menu={"items": items},
    )
