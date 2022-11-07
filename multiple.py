import reflect as r
import reflect_antd as antd
import reflect_html as html


def handle_menu_click(key):
    print("click", key)


def app():
    def build_menu():
        return [
            antd.Menu.Item("1st item", key="1"),
            antd.Menu.Item("2nd item", key="2"),
            antd.Menu.Item("3rd item", key="3"),
        ]

    menu = antd.Menu(build_menu, onClick=r.Callback(handle_menu_click, "key"))
    menu1 = antd.Menu(
        [
            antd.Menu.Item("1st item", key="1"),
            antd.Menu.Item("2nd item", key="2"),
            antd.Menu.Item("3rd item", key="3"),
        ],
        onClick=r.Callback(handle_menu_click, "key"),
    )
    return div(
        [
            antd.Button("primary", type="primary"),
            antd.Button("secondary"),
            menu,
            antd.Dropdown.Button("Actions", overlay=menu),
        ]
    )
