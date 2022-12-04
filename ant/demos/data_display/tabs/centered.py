import reflect_antd as antd
import reflect_html as html

TabPane = antd.Tabs.TabPane


def app():
    return antd.Tabs(
        [
            TabPane("Content of Tab Pane 1", tab="Tab 1", key="1"),
            TabPane("Content of Tab Pane 2", tab="Tab 2", key="2"),
            TabPane("Content of Tab Pane 3", tab="Tab 3", key="3"),
        ],
        defaultActiveKey="1",
        centered=True,
    )
