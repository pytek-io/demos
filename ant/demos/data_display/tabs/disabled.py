import reflect_antd as antd
import reflect_html as html

TabPane = antd.Tabs.TabPane


def app():
    return antd.Tabs(
        [
            TabPane("Tab 1 content", tab="Tab 1", key="1"),
            TabPane("Tab 2 content", tab="Tab 2", disabled=True, key="2"),
            TabPane("Tab 3 content", tab="Tab 3", key="3"),
        ],
        defaultActiveKey="1",
    )
