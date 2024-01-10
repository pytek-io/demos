import render_antd as antd


def app(_):
    items = [
        {"label": "1st item", "key": "1"},
        {"label": "2nd item", "key": "2"},
        {"label": "3rd item", "key": "3"},
    ]
    return antd.Space(
        [
            antd.Button("primary", type="primary"),
            antd.Button("secondary"),
            antd.Dropdown.Button(
                "Actions",
                menu=antd.MenuProps(
                    items=items, onClick=lambda key: print("click", key)
                ),
            ),
        ]
    )
