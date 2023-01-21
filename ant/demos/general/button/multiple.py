import reflect as r
import reflect_antd as antd
import reflect_html as html


def handle_menu_click(key):
    print("click", key)


def app():
    items = [
        {"label": "1st item", "key": "1"},
        {"label": "2nd item", "key": "2"},
        {"label": "3rd item", "key": "3"},
    ]
    return html.div(
        [
            antd.Button("primary", type="primary"),
            antd.Button("secondary"),
            antd.Dropdown.Button(
                "Actions",
                menu={"items": items, "onClick": r.Callback(handle_menu_click, "key")},
            ),
        ]
    )
