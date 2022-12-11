import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

import reflect as r


def app():
    openKeys = r.ObservableList(["sub1"])

    def onOpenChange(keys):
        latestOpenKey = next((key for key in keys if key not in openKeys), None)
        if latestOpenKey not in rootSubmenuKeys:
            openKeys.set(keys)
        else:
            openKeys.set([latestOpenKey] if latestOpenKey else [])

    return html.div(
        [
            antd.Menu(
                [
                    {
                        "children": [
                            antd.Menu.Item("Option 1", key="1"),
                            antd.Menu.Item("Option 2", key="2"),
                            antd.Menu.Item("Option 3", key="3"),
                            antd.Menu.Item("Option 4", key="4"),
                        ],
                        "key": "sub1",
                        "icon": ant_icons.MailOutlined([]),
                        "label": "Navigation One",
                    },
                    {
                        "children": [
                            antd.Menu.Item("Option 5", key="5"),
                            antd.Menu.Item("Option 6", key="6"),
                            {
                                "children": [
                                    antd.Menu.Item("Option 7", key="7"),
                                    antd.Menu.Item("Option 8", key="8"),
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
                            antd.Menu.Item("Option 9", key="9"),
                            antd.Menu.Item("Option 10", key="10"),
                            antd.Menu.Item("Option 11", key="11"),
                            antd.Menu.Item("Option 12", key="12"),
                        ],
                        "key": "sub4",
                        "icon": ant_icons.SettingOutlined([]),
                        "label": "Navigation Three",
                    },
                ],
                mode="inline",
                openKeys=openKeys,
                onOpenChange=r.Callback(onOpenChange),
                style=dict(width=256),
            )
        ]
    )
