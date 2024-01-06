import render_antd as antd
import render_html as html


def app():
    OperationsSlot = {
        "left": antd.Button("Left Extra Action", className="tabs-extra-demo-button"),
        "right": antd.Button("Right Extra Action"),
    }
    operations = antd.Button("Extra Action")
    options = ["left", "right"]
    position = antd.CheckboxGroup(options=options, defaultValue=options)

    def slot():
        return {direction: OperationsSlot[direction] for direction in position()} or []

    return html.div(
        [
            antd.Tabs(
                items=[
                    {"children": "Content of tab 1", "label": "Tab 1", "key": "1"},
                    {"children": "Content of tab 2", "label": "Tab 2", "key": "2"},
                    {"children": "Content of tab 3", "label": "Tab 3", "key": "3"},
                ],
                tabBarExtraContent=operations,
            ),
            html.br(),
            html.br(),
            html.br(),
            html.div("You can also specify its direction or both side"),
            antd.Divider(),
            position,
            html.br(),
            html.br(),
            antd.Tabs(
                items=[
                    {"children": "Content of tab 1", "label": "Tab 1", "key": "1"},
                    {"children": "Content of tab 2", "label": "Tab 2", "key": "2"},
                    {"children": "Content of tab 3", "label": "Tab 3", "key": "3"},
                ],
                tabBarExtraContent=slot,
            ),
        ]
    )
