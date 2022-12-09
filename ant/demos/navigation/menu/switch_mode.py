import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    switch_mode = antd.Switch("vertical mode", defaultChecked=False)
    switch_theme = antd.Switch("dark theme", defaultChecked=False)
    mode = lambda: "vertical" if switch_mode() else "inline"
    theme = lambda: "dark" if switch_theme() else "light"
    return html.div(
        [
            switch_mode,
            antd.Divider(type="vertical"),
            switch_theme,
            html.br(),
            html.br(),
            antd.Menu(
                items=[
                    {
                        "label": "Navigation One",
                        "key": "1",
                        "icon": ant_icons.MailOutlined([]),
                    },
                    {
                        "label": "Navigation Two",
                        "key": "2",
                        "icon": ant_icons.CalendarOutlined([]),
                    },
                    {
                        "children": [
                            {"label": "Option 3", "key": "3"},
                            {"label": "Option 4", "key": "4"},
                            {
                                "children": [
                                    {"label": "Option 5", "key": "5"},
                                    {"label": "Option 6", "key": "6"},
                                ],
                                "key": "sub1-2",
                                "label": "Submenu",
                            },
                        ],
                        "key": "sub1",
                        "icon": ant_icons.AppstoreOutlined([]),
                        "label": "Navigation Two",
                    },
                    {
                        "children": [
                            {"label": "Option 7", "key": "7"},
                            {"label": "Option 8", "key": "8"},
                            {"label": "Option 9", "key": "9"},
                            {"label": "Option 10", "key": "10"},
                        ],
                        "key": "sub2",
                        "icon": ant_icons.SettingOutlined([]),
                        "label": "Navigation Three",
                    },
                    {
                        "label": html.a(
                            "Ant Design",
                            href="https://ant.design",
                            target="_blank",
                            rel="noopener noreferrer",
                        ),
                        "key": "link",
                        "icon": ant_icons.LinkOutlined([]),
                    },
                ],
                style=dict(width=256),
                defaultSelectedKeys=["1"],
                defaultOpenKeys=["sub1"],
                mode=mode,
                theme=theme,
            ),
        ]
    )
