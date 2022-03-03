from reflect_html import *
from reflect_antd import Tabs
from reflected.react.sticky import StickyContainer, Sticky
TabPane = Tabs.TabPane
renderTabBar = Sticky([""{( style ) => (", DefaultTabBar("{...props}"=True, className="site-custom-tab-bar", style=dict()), ")}""], bottomOffset=80)
def app():
    return StickyContainer(Tabs([TabPane("Content of Tab Pane 1", tab="Tab 1", key="1", style=dict(height=200)), TabPane("Content of Tab Pane 2", tab="Tab 2", key="2"), TabPane("Content of Tab Pane 3", tab="Tab 3", key="3")], defaultActiveKey="1", renderTabBar=renderTabBar))