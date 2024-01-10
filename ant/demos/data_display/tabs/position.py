import render_antd as antd
import render_html as html


def app(_):
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
            antd.Space(["Tab position:", tabPosition], style={"marginBottom": 24}),
            antd.Tabs(
                items=[
                    {"children": "Content of Tab 1", "label": "Tab 1", "key": "1"},
                    {"children": "Content of Tab 2", "label": "Tab 2", "key": "2"},
                    {"children": "Content of Tab 3", "label": "Tab 3", "key": "3"},
                ],
                tabPosition=tabPosition,
            ),
        ]
    )
