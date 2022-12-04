import reflect_antd as antd
import reflect_html as html

TabPane = antd.Tabs.TabPane


def app():
    size = antd.Radio.Group(
        [
            antd.Radio.Button("Small", value="small"),
            antd.Radio.Button("Default", value="default"),
            antd.Radio.Button("Large", value="large"),
        ],
        defaultValue="small",
        style=dict(marginBottom=16),
    )
    return html.div(
        [
            size,
            antd.Tabs(
                [
                    TabPane("Content of tab 1", tab="Tab 1", key="1"),
                    TabPane("Content of tab 2", tab="Tab 2", key="2"),
                    TabPane("Content of tab 3", tab="Tab 3", key="3"),
                ],
                defaultActiveKey="1",
                size=size,
                style=dict(marginBottom=32),
            ),
            antd.Tabs(
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
