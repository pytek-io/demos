from render_antd import Layout, Menu
from render_html import *

Header, Sider, Content = Layout.Header, Layout.Sider, Layout.Content
def app(_):
    return Layout([Sider([div(className="logo"), Menu([Menu.Item("nav 1", key="1", icon=UserOutlined([])), Menu.Item("nav 2", key="2", icon=VideoCameraOutlined([])), Menu.Item("nav 3", key="3", icon=UploadOutlined([]))], theme="dark", mode="inline", defaultSelectedKeys=['1'])], trigger=null, collapsible=True, collapsed=this.state.collapsed), Layout([Header(""{React.createElement(this.state.collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, "{               className: 'trigger',               onClick: this.toggle,             )}"", className="site-layout-background", style=dict(padding=0)), Content("Content", className="site-layout-background", style=dict(margin='24px 16px', padding=24, minHeight=280))], className="site-layout")])
def app(_):
    return SiderDemo()