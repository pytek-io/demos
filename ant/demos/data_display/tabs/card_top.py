import render_antd as antd
import render_html as html


def app():
    return html.div(
        antd.Tabs(
            items=[
                {
                    "children": [
                        html.p("Content of Tab Pane 1"),
                        html.p("Content of Tab Pane 1"),
                        html.p("Content of Tab Pane 1"),
                    ],
                    "label": "Tab Title 1",
                    "key": "1",
                },
                {
                    "children": [
                        html.p("Content of Tab Pane 2"),
                        html.p("Content of Tab Pane 2"),
                        html.p("Content of Tab Pane 2"),
                    ],
                    "label": "Tab Title 2",
                    "key": "2",
                },
                {
                    "children": [
                        html.p("Content of Tab Pane 3"),
                        html.p("Content of Tab Pane 3"),
                        html.p("Content of Tab Pane 3"),
                    ],
                    "label": "Tab Title 3",
                    "key": "3",
                },
            ],
            type="card",
        ),
        className="card-container",
    )
