import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

items = [
    {
        "type": "group",
        "children": [{"label": "1st menu item"}, {"label": "2nd menu item"}],
        "label": "Group title",
    },
    {
        "children": [{"label": "3rd menu item"}, {"label": "4th menu item"}],
        "label": "sub menu",
    },
    {
        "children": [{"label": "5d menu item"}, {"label": "6th menu item"}],
        "label": "disabled sub menu",
        "disabled": True,
    },
]


def app():
    return antd.Dropdown(
        html.a(
            ["Cascading menu", ant_icons.DownOutlined()],
            className="ant-dropdown-link",
            onClick=lambda e: e.preventDefault(),
        ),
        menu={"items": items},
    )
