import reflect_antd as antd
import reflect_html as html

TabPane = antd.Tabs.TabPane


def app():
    return html.div(
        antd.Tabs(
            [
                TabPane(
                    [
                        html.p("Content of Tab Pane 1"),
                        html.p("Content of Tab Pane 1"),
                        html.p("Content of Tab Pane 1"),
                    ],
                    tab="Tab Title 1",
                    key="1",
                ),
                TabPane(
                    [
                        html.p("Content of Tab Pane 2"),
                        html.p("Content of Tab Pane 2"),
                        html.p("Content of Tab Pane 2"),
                    ],
                    tab="Tab Title 2",
                    key="2",
                ),
                TabPane(
                    [
                        html.p("Content of Tab Pane 3"),
                        html.p("Content of Tab Pane 3"),
                        html.p("Content of Tab Pane 3"),
                    ],
                    tab="Tab Title 3",
                    key="3",
                ),
            ],
            type="card",
        ),
        className="card-container",
    )
