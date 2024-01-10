from render_ant_icons import AppstoreOutlined, MailOutlined, SettingOutlined
from render_antd import Menu, Switch
from render_html import *

SubMenu = Menu.SubMenu
def app(_):
    return[
 Switch(checked=this.state.theme === 'dark', onChange=this.changeTheme, checkedChildren="Dark", unCheckedChildren="Light"),
 br(),
 br(),
 Menu([SubMenu([Menu.Item("Option 1", key="1"), Menu.Item("Option 2", key="2"), Menu.Item("Option 3", key="3"), Menu.Item("Option 4", key="4")], key="sub1", icon=MailOutlined([]), title="Navigation One"), SubMenu([Menu.Item("Option 5", key="5"), Menu.Item("Option 6", key="6"), SubMenu([Menu.Item("Option 7", key="7"), Menu.Item("Option 8", key="8")], key="sub3", title="Submenu")], key="sub2", icon=AppstoreOutlined([]), title="Navigation Two"), SubMenu([Menu.Item("Option 9", key="9"), Menu.Item("Option 10", key="10"), Menu.Item("Option 11", key="11"), Menu.Item("Option 12", key="12")], key="sub4", icon=SettingOutlined([]), title="Navigation Three")], theme=this.state.theme, onClick=this.handleClick, style=dict(width=256), defaultOpenKeys=['sub1'], selectedKeys=[this.state.current], mode="inline"),
]
def app(_):
    return Sider()