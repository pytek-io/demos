from render_ant_icons import UploadOutlined, UserOutlined, VideoCameraOutlined
from render_antd import Layout, Menu
from render_html import *

Header, Content, Footer, Sider = Layout.Header, Layout.Content, Layout.Footer, Layout.Sider
def app(_):
    return Layout([Sider([div(className="logo"), Menu([Menu.Item("nav 1", key="1", icon=UserOutlined([])), Menu.Item("nav 2", key="2", icon=VideoCameraOutlined([])), Menu.Item("nav 3", key="3", icon=UploadOutlined([])), Menu.Item("nav 4", key="4", icon=UserOutlined([]))], theme="dark", mode="inline", defaultSelectedKeys=['4'])], breakpoint="lg", collapsedWidth="0", onBreakpoint="{broken => ", {=True, print(broken);=True, !}"=True, onCollapse="{(collapsed, type) => ", {=True, print(collapsed,=True, type);=True, !}"=True), Layout([Header(className="site-layout-sub-header-background", style=dict(padding=0)), Content(div("content", className="site-layout-background", style=dict(padding=24, minHeight=360)), style=dict(margin='24px 16px 0')), Footer("Ant Design ©2018 Created by Ant UED", style=dict(textAlign='center'))])])