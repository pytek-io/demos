from reflect_html import *
from reflect_antd import Tabs

TabPane = Tabs.TabPane


def app():
    return div(
        Tabs(
            [
                TabPane(
                    [
                        p("Content of Tab Pane 1"),
                        p("Content of Tab Pane 1"),
                        p("Content of Tab Pane 1"),
                    ],
                    tab="Tab Title 1",
                    key="1",
                ),
                TabPane(
                    [
                        p("Content of Tab Pane 2"),
                        p("Content of Tab Pane 2"),
                        p("Content of Tab Pane 2"),
                    ],
                    tab="Tab Title 2",
                    key="2",
                ),
                TabPane(
                    [
                        p("Content of Tab Pane 3"),
                        p("Content of Tab Pane 3"),
                        p("Content of Tab Pane 3"),
                    ],
                    tab="Tab Title 3",
                    key="3",
                ),
            ],
            type="card",
        ),
        className="card-container",
    )
