import reflect_antd as antd
import reflect_html as html


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
                items=[
                    {"children": "Content of tab 1", "label": "Tab 1", "key": "1"},
                    {"children": "Content of tab 2", "label": "Tab 2", "key": "2"},
                    {"children": "Content of tab 3", "label": "Tab 3", "key": "3"},
                ],
                defaultActiveKey="1",
                size=size,
                style=dict(marginBottom=32),
            ),
            antd.Tabs(
                items=[
                    {
                        "children": "Content of card tab 1",
                        "label": "Card Tab 1",
                        "key": "1",
                    },
                    {
                        "children": "Content of card tab 2",
                        "label": "Card Tab 2",
                        "key": "2",
                    },
                    {
                        "children": "Content of card tab 3",
                        "label": "Card Tab 3",
                        "key": "3",
                    },
                ],
                defaultActiveKey="1",
                type="card",
                size=size,
            ),
        ]
    )
