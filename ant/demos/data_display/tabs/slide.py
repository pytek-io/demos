import reflect_antd as antd
import reflect_html as html

TabPane = antd.Tabs.TabPane


def app():
    mode = antd.Radio.Group(
        [
            antd.Radio.Button("Horizontal", value="top"),
            antd.Radio.Button("Vertical", value="left"),
        ],
        defaultValue="top",
        style=dict(marginBottom=8),
    )
    return html.div(
        [
            mode,
            antd.Tabs(
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
