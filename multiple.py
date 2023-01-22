import reflect as r
import reflect_antd as antd


def handle_menu_click(key):
    print("click", key)


def app():
    def build_menu():
        return [
            {"label": "1st item", "key": "1"},
            {"label": "2nd item", "key": "2"},
            {"label": "3rd item", "key": "3"},
        ]

    menu = antd.Menu(items=build_menu, onClick=r.Callback(handle_menu_click, "key"))
    menu1 = antd.Menu(
        items=[
            {"label": "1st item", "key": "1"},
            {"label": "2nd item", "key": "2"},
            {"label": "3rd item", "key": "3"},
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
