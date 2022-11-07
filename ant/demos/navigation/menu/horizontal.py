import reflect as r
import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

SubMenu = antd.Menu.SubMenu


def app():
    current = r.create_observable("mail")

    def handleClick(value):
        print(f"clicked {value}")
        current.set(value)

    return html.div(
        [
            antd.Menu(
                [
                    antd.Menu.Item("Mail", key="mail", icon=ant_icons.MailOutlined()),
                    antd.Menu.Item(
                        "AppStore", key="app_store", icon=ant_icons.AppstoreOutlined()
                    ),
                    antd.Menu.Item(
                        "Settings", key="settings", icon=ant_icons.SettingOutlined()
                    ),
                ],
                onClick=r.Callback(handleClick, args="key"),
            ),
            html.div(current),
        ]
    )
