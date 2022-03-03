from reflect_html import *
from reflect_antd import Tabs, Radio

TabPane = Tabs.TabPane


def app():

    size  = Radio.Group(
                [
                    Radio.Button("Small", value="small"),
                    Radio.Button("Default", value="default"),
                    Radio.Button("Large", value="large"),
                ],
                defaultValue="small",
                style=dict(marginBottom=16),
            )
    return div(
        [
            size,
            Tabs(
                [
                    TabPane("Content of tab 1", tab="Tab 1", key="1"),
                    TabPane("Content of tab 2", tab="Tab 2", key="2"),
                    TabPane("Content of tab 3", tab="Tab 3", key="3"),
                ],
                defaultActiveKey="1",
                size=size,
                style=dict(marginBottom=32),
            ),
            Tabs(
                [
                    TabPane("Content of card tab 1", tab="Card Tab 1", key="1"),
                    TabPane("Content of card tab 2", tab="Card Tab 2", key="2"),
                    TabPane("Content of card tab 3", tab="Card Tab 3", key="3"),
                ],
                defaultActiveKey="1",
                type="card",
                size=size,
            ),
        ]
    )
