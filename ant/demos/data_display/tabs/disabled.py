from reflect_html import *
from reflect_antd import Tabs

TabPane = Tabs.TabPane


def app():
    return Tabs(
        [
            TabPane("Tab 1 content", tab="Tab 1", key="1"),
            TabPane("Tab 2 content", tab="Tab 2", disabled=True, key="2"),
            TabPane("Tab 3 content", tab="Tab 3", key="3"),
        ],
        defaultActiveKey="1",
    )
