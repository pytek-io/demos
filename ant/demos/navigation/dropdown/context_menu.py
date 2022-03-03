from reflect_html import *
from reflect_antd import Menu, Dropdown

menu = Menu(
    [
        Menu.Item("1st menu item", key="1", onClick= lambda: print("hello")),
        Menu.Item("2nd menu item", key="2"),
        Menu.Item("3rd menu item", key="3"),
    ]
)


def app():
    return Dropdown(
        div(
            "Right Click on here",
            className="site-dropdown-context-menu",
            style=dict(textAlign="center", height=200, lineHeight="200px"),
        ),
        overlay=menu,
        trigger=["contextMenu"],
    )
