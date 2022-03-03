from reflect_html import *
from reflect_antd import Tabs

TabPane = Tabs.TabPane


def app():
    return Tabs(
        [
            TabPane("Content of Tab Pane 1", tab="Tab 1", key="1"),
            TabPane("Content of Tab Pane 2", tab="Tab 2", key="2"),
            TabPane("Content of Tab Pane 3", tab="Tab 3", key="3"),
        ],
        defaultActiveKey="1",
        centered=True,
    )
