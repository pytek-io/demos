from reflect_html import *
from reflect_antd import Row, Col, Divider


def app():
    return div([
        Divider("Percentage columns", orientation="left"),
        Row([Col("2 / 5", flex=2), Col("3 / 5", flex=3)]),
        Divider("Fill rest", orientation="left"),
        Row([Col("100px", flex="100px"), Col("Fill Rest", flex="auto")]),
        Divider("Raw flex style", orientation="left"),
        Row([Col("1 1 200px", flex="1 1 200px"), Col("0 1 300px", flex="0 1 300px")]),
        Row(
            [
                Col(div("none", style=dict(padding="0 16px")), flex="none"),
                Col("auto with no-wrap", flex="auto"),
            ],
            wrap=False,
        ),
    ]
)