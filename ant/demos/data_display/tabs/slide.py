from reflect_html import *
from reflect_antd import Tabs, Radio

TabPane = Tabs.TabPane


def app():
    mode = Radio.Group(
        [
            Radio.Button("Horizontal", value="top"),
            Radio.Button("Vertical", value="left"),
        ],
        defaultValue="top",
        style=dict(marginBottom=8),
    )
    return div(
        [
            mode,
            Tabs(
                [
                    TabPane(
                        f"Content of tab {i}", tab=f"Tab-{i}", key=i, disabled=i == 28
                    )
                    for i in range(1, 30)
                ],
                defaultActiveKey="3",
                tabPosition=mode,
                style=dict(height=220),
            ),
        ]
    )
