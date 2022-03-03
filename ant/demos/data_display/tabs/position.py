from reflect_html import *
from reflect_antd import Tabs, Radio, Space

TabPane = Tabs.TabPane


def app():
    tabPosition = Radio.Group(
        [
            Radio.Button("top", value="top"),
            Radio.Button("bottom", value="bottom"),
            Radio.Button("left", value="left"),
            Radio.Button("right", value="right"),
        ],
        defaultValue="left",
    )
    return [
        Space(
            [
                "Tab position:",
                tabPosition,
            ],
            style=dict(marginBottom=24),
        ),
        Tabs(
            [
                TabPane("Content of Tab 1", tab="Tab 1", key="1"),
                TabPane("Content of Tab 2", tab="Tab 2", key="2"),
                TabPane("Content of Tab 3", tab="Tab 3", key="3"),
            ],
            tabPosition=tabPosition,
        ),
    ]
