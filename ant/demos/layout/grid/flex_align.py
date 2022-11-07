from reflect_html import *
from reflect_antd import Row, Col, Divider


class DemoBox(p):
    JSXName = "p"

    def __init__(self, children, value: int, *arg):
        # kwargs["className"] = f"height-{value}"
        super().__init__(children, *arg)


def app():
    return div(
        [
            Divider("Align Top", orientation="left"),
            Row(
                [
                    Col(DemoBox("col-4", value=100), span=4),
                    Col(DemoBox("col-4", value=50), span=4),
                    Col(DemoBox("col-4", value=120), span=4),
                    Col(DemoBox("col-4", value=80), span=4),
                ],
                justify="center",
                align="top",
            ),
            Divider("Align Middle", orientation="left"),
            Row(
                [
                    Col(DemoBox("col-4", value=100), span=4),
                    Col(DemoBox("col-4", value=50), span=4),
                    Col(DemoBox("col-4", value=120), span=4),
                    Col(DemoBox("col-4", value=80), span=4),
                ],
                justify="space-around",
                align="middle",
            ),
            Divider("Align Bottom", orientation="left"),
            Row(
                [
                    Col(DemoBox("col-4", value=100), span=4),
                    Col(DemoBox("col-4", value=50), span=4),
                    Col(DemoBox("col-4", value=120), span=4),
                    Col(DemoBox("col-4", value=80), span=4),
                ],
                justify="space-between",
                align="bottom",
            ),
        ]
    )
