import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

import reflect as r


def app():
    return antd.Menu(
        items=[
            {
                "children": [
                    {
                        "type": "group",
                        "children": [
                            {"label": "Option 1", "key": "1"},
                            {"label": "Option 2", "key": "2"},
                        ],
                        "label": "Item 1",
                    },
                    {
                        "type": "group",
                        "children": [
                            {"label": "Option 3", "key": "3"},
                            {"label": "Option 4", "key": "4"},
                        ],
                        "label": "Item 2",
                    },
                ],
                "key": "sub1",
                "icon": ant_icons.MailOutlined(),
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
                "icon": ant_icons.AppstoreOutlined(),
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
                "icon": ant_icons.SettingOutlined(),
                "label": "Navigation Three",
            },
        ],
        onClick=r.Callback(lambda key: print(f"clicked {key}"), args="key"),
        style=dict(width=256),
        mode="vertical",
    )
