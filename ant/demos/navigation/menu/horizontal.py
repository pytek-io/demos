from reflect_html import *
from reflect_antd import Menu
from reflect_ant_icons import MailOutlined, AppstoreOutlined, SettingOutlined
from reflect import Callback, create_observable

SubMenu = Menu.SubMenu


def app():
    current = create_observable("mail")

    def handleClick(value):
        print(f"clicked {value}")
        current.set(value)

    return div(
        [
            Menu(
                [
                    Menu.Item("Mail", key="mail", icon=MailOutlined()),
                    Menu.Item("AppStore", key="app_store", icon=AppstoreOutlined()),
                    Menu.Item("Settings", key="settings", icon=SettingOutlined()),
                ],
                onClick=Callback(handleClick, args="key"),
            ),
            div(current),
        ]
    )
