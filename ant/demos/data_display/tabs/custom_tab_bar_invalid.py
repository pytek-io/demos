from render_antd import Tabs
from render_html import *
from rendered.react.sticky import Sticky, StickyContainer

TabPane = Tabs.TabPane
renderTabBar = Sticky([""{( style ) => (", DefaultTabBar("{...props}"=True, className="site-custom-tab-bar", style=dict()), ")}""], bottomOffset=80)
def app(_):
    return StickyContainer(Tabs([TabPane("Content of Tab Pane 1", tab="Tab 1", key="1", style=dict(height=200)), TabPane("Content of Tab Pane 2", tab="Tab 2", key="2"), TabPane("Content of Tab Pane 3", tab="Tab 3", key="3")], defaultActiveKey="1", renderTabBar=renderTabBar))