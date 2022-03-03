from reflect_html import *
from reflect_antd import Menu, Button
SubMenu = Menu.SubMenu
def app():
    return div([Button(""{React.createElement(this.state.collapsed ? MenuUnfoldOutlined : MenuFoldOutlined)}"", type="primary", onClick=this.toggleCollapsed, style=dict(marginBottom=16)), Menu([Menu.Item("Option 1", key="1", icon=PieChartOutlined([])), Menu.Item("Option 2", key="2", icon=DesktopOutlined([])), Menu.Item("Option 3", key="3", icon=ContainerOutlined([])), SubMenu([Menu.Item("Option 5", key="5"), Menu.Item("Option 6", key="6"), Menu.Item("Option 7", key="7"), Menu.Item("Option 8", key="8")], key="sub1", icon=MailOutlined([]), title="Navigation One"), SubMenu([Menu.Item("Option 9", key="9"), Menu.Item("Option 10", key="10"), SubMenu([Menu.Item("Option 11", key="11"), Menu.Item("Option 12", key="12")], key="sub3", title="Submenu")], key="sub2", icon=AppstoreOutlined([]), title="Navigation Two")], defaultSelectedKeys=['1'], defaultOpenKeys=['sub1'], mode="inline", theme="dark", inlineCollapsed=this.state.collapsed)], style=dict(width=256))
def app():
    return App()