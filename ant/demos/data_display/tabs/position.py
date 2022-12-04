import reflect_antd as antd
import reflect_html as html

TabPane = antd.Tabs.TabPane


def app():
    tabPosition = antd.Radio.Group(
        [
            antd.Radio.Button("top", value="top"),
            antd.Radio.Button("bottom", value="bottom"),
            antd.Radio.Button("left", value="left"),
            antd.Radio.Button("right", value="right"),
        ],
        defaultValue="left",
    )
    return html.div(
        [
            antd.Space(["Tab position:", tabPosition], style=dict(marginBottom=24)),
            antd.Tabs(
                [
                    TabPane("Content of Tab 1", tab="Tab 1", key="1"),
                    TabPane("Content of Tab 2", tab="Tab 2", key="2"),
                    TabPane("Content of Tab 3", tab="Tab 3", key="3"),
                ],
                tabPosition=tabPosition,
            ),
        ]
    )
