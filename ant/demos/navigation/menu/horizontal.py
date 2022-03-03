from reflect_html import *
from reflect_antd import Menu
from reflect_ant_icons import MailOutlined, AppstoreOutlined, SettingOutlined
from reflect import Callback
from reflect import make_observable

SubMenu = Menu.SubMenu


def app():
    current = make_observable("mail")

    def handleClick(value):
        print("click ", value)
        current.set(value)

    return Menu(
            [
                Menu.Item("Navigation One", key="mail", icon=MailOutlined()),
            ],
        )
