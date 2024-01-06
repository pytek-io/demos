import render_antd as antd
import render_html as html

items = [
    {"label": "1st menu item", "key": "1", "onClick": lambda: print("hello")},
    {"label": "2nd menu item", "key": "2"},
    {"label": "3rd menu item", "key": "3"},
]


def app():
    return antd.Dropdown(
        html.div(
            "Right Click on here",
            className="site-dropdown-context-menu",
            style=dict(textAlign="center", height=200, lineHeight="200px"),
        ),
        menu={"items": items},
        trigger=["contextMenu"],
    )
