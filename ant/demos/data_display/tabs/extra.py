from reflect_html import *
from reflect_antd import Tabs, Button, Divider, CheckboxGroup
from reflect import js

TabPane = Tabs.TabPane


def app():

    OperationsSlot = {
        "left": Button("Left Extra Action", className="tabs-extra-demo-button"),
        "right": Button("Right Extra Action"),
    }

    operations = Button("Extra Action")
    options = ["left", "right"]
    position = CheckboxGroup(options=options, defaultValue=options)

    def slot():
        return {direction: OperationsSlot[direction] for direction in position()} or []

    return [
        Tabs(
            [
                TabPane("Content of tab 1", tab="Tab 1", key="1"),
                TabPane("Content of tab 2", tab="Tab 2", key="2"),
                TabPane("Content of tab 3", tab="Tab 3", key="3"),
            ],
            tabBarExtraContent=operations,
        ),
        br(),
        br(),
        br(),
        div("You can also specify its direction or both side"),
        Divider(),
        position,
        br(),
        br(),
        Tabs(
            [
                TabPane("Content of tab 1", tab="Tab 1", key="1"),
                TabPane("Content of tab 2", tab="Tab 2", key="2"),
                TabPane("Content of tab 3", tab="Tab 3", key="3"),
            ],
            tabBarExtraContent=slot,
        ),
    ]
