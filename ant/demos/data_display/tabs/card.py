import render_antd as antd

items = [
    {"label": "Tab 1", "key": "item-1", "children": "Content 1"},
    {"label": "Tab 2", "key": "item-2", "children": "Content 2"},
]


def app(_):
    return antd.Tabs(
        items=items, onChange=print, defaultActiveKey="item-2", type="card"
    )
