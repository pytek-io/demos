import render_antd as antd


def app(_):
    return antd.Tabs(
        items=[
            {"children": "Content of Tab Pane 1", "label": "Tab 1", "key": "1"},
            {"children": "Content of Tab Pane 2", "label": "Tab 2", "key": "2"},
            {"children": "Content of Tab Pane 3", "label": "Tab 3", "key": "3"},
        ],
        defaultActiveKey="1",
        onChange=print,
    )
