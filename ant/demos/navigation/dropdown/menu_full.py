import reflect as r
import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

menu = {
    "items": [
        {
            "type": "group",
            "children": [
                {"label": "Option 0", "key": "01"},
                {"label": "Option 0", "key": "02"},
            ],
            "key": "group",
            "label": "Item Group",
        },
        {
            "children": [
                {
                    "type": "group",
                    "children": [
                        {"label": "Option 1", "key": "1"},
                        {"label": "Option 2", "key": "2"},
                    ],
                    "key": "g1",
                    "label": "Item 1",
                },
                {
                    "type": "group",
                    "children": [
                        {"label": "Option 3", "key": "3"},
                        {"label": "Option 4", "key": "4"},
                    ],
                    "key": "g2",
                    "label": "Item 2",
                },
            ],
            "key": "sub1",
            "icon": ant_icons.MailOutlined([]),
            "label": "Navigation One",
        },
        {
            "children": [
                {"label": "Option 5", "key": "5"},
                {"label": "Option 6", "key": "6"},
                {
                    "children": [
                        {"label": "Option 7", "key": "7"},
                        {"label": "Option 8", "key": "8"},
                    ],
                    "key": "sub3",
                    "label": "Submenu",
                },
            ],
            "key": "sub2",
            "icon": ant_icons.AppstoreOutlined([]),
            "label": "Navigation Two",
        },
        {
            "children": [
                {"label": "Option 9", "key": "9"},
                {"label": "Option 10", "key": "10"},
                {"label": "Option 11", "key": "11"},
                {"label": "Option 12", "key": "12"},
            ],
            "key": "sub4",
            "icon": ant_icons.SettingOutlined([]),
            "label": "Navigation Three",
        },
    ],
    "onClick": r.Callback(lambda x: print("clicked", x[0]), args=("key",)),
    # "selectedKeys": ["1"],
    # "openKeys": ["sub1"],
}


def app():
    return antd.Dropdown(
        html.a(
            ["Hover to check menu style", ant_icons.DownOutlined()],
            className="ant-dropdown-link",
            onClick=lambda e: e.preventDefault(),
        ),
        menu=menu,
    )
