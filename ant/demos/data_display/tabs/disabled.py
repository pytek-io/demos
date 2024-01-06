import render_antd as antd


def app():
    return antd.Tabs(
        items=[
            {"children": "Tab 1 content", "label": "Tab 1", "key": "1"},
            {
                "children": "Tab 2 content",
                "label": "Tab 2",
                "disabled": True,
                "key": "2",
            },
            {"children": "Tab 3 content", "label": "Tab 3", "key": "3"},
        ],
        defaultActiveKey="1",
    )
