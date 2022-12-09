import reflect as r
import reflect_antd as antd

TabPane = antd.Tabs.TabPane


def callback(key):
    print(key)


def app():
    return antd.Tabs(
        [
            TabPane("Content of Tab Pane 1", tab="Tab 1", key="1"),
            TabPane("Content of Tab Pane 2", tab="Tab 2", key="2"),
            TabPane("Content of Tab Pane 3", tab="Tab 3", key="3"),
        ],
        defaultActiveKey="1",
        onChange=r.Callback(callback),
    )
