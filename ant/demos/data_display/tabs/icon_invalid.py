from reflect_html import *
from reflect_antd import Tabs
from reflect_ant_icons import AppleOutlined, AndroidOutlined
TabPane = Tabs.TabPane
def app():
    return Tabs([TabPane("Tab 1", tab=<span>           <AppleOutlined />           Tab 1         </span>, key="1"), TabPane("Tab 2", tab=<span>           <AndroidOutlined />           Tab 2         </span>, key="2")], defaultActiveKey="2")