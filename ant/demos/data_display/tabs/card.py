import reflect as r
import reflect_antd as antd

TabPane = antd.Tabs.TabPane


def callback(key):
    print(key)


items = [
    {"label": "Tab 1", "key": "item-1", "children": "Content 1"},
    {"label": "Tab 2", "key": "item-2", "children": "Content 2"},
]


def app():
    return antd.Tabs(
        items=items,
        # onChange=r.Callback(callback),
        # onTabChange=r.Callback(callback),
        defaultActiveKey="item-2",
        # type="card",
        key="whatever"
    )
