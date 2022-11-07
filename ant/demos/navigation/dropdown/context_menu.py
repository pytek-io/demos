import reflect_antd as antd
import reflect_html as html

menu = antd.Menu(
    [
        antd.Menu.Item("1st menu item", key="1", onClick=lambda: print("hello")),
        antd.Menu.Item("2nd menu item", key="2"),
        antd.Menu.Item("3rd menu item", key="3"),
    ]
)


def app():
    return antd.Dropdown(
        html.div(
            "Right Click on here",
            className="site-dropdown-context-menu",
            style=dict(textAlign="center", height=200, lineHeight="200px"),
        ),
        overlay=menu,
        trigger=["contextMenu"],
    )
