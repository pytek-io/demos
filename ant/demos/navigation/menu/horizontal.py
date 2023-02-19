import reflect as r
import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    current = r.ObservableValue("mail")

    def handleClick(value):
        print(f"clicked {value}")
        current.set(value)

    return html.div(
        [
            antd.Menu(
                items=[
                    {"label": "Mail", "key": "mail", "icon": ant_icons.MailOutlined()},
                    {
                        "label": "AppStore",
                        "key": "app_store",
                        "icon": ant_icons.AppstoreOutlined(),
                    },
                    {
                        "label": "Settings",
                        "key": "settings",
                        "icon": ant_icons.SettingOutlined(),
                    },
                ],
                onClick=handleClick,
            ),
            html.div(current),
        ]
    )
