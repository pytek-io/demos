from render_ant_icons import AndroidOutlined, AppleOutlined
from render_antd import Tabs
from render_html import *

TabPane = Tabs.TabPane
def app(_):
    return Tabs([TabPane("Tab 1", tab=<span>           <AppleOutlined />           Tab 1         </span>, key="1"), TabPane("Tab 2", tab=<span>           <AndroidOutlined />           Tab 2         </span>, key="2")], defaultActiveKey="2")