import render_antd as antd
import render_html as html


class DemoBox(html.p):
    JSXName = "p"

    def __init__(self, children, value: int, *arg):
        super().__init__(children, *arg)


def app(_):
    return html.div(
        [
            antd.Divider("Align Top", orientation="left"),
            antd.Row(
                [
                    antd.Col(DemoBox("col-4", value=100), span=4),
                    antd.Col(DemoBox("col-4", value=50), span=4),
                    antd.Col(DemoBox("col-4", value=120), span=4),
                    antd.Col(DemoBox("col-4", value=80), span=4),
                ],
                justify="center",
                align="top",
            ),
            antd.Divider("Align Middle", orientation="left"),
            antd.Row(
                [
                    antd.Col(DemoBox("col-4", value=100), span=4),
                    antd.Col(DemoBox("col-4", value=50), span=4),
                    antd.Col(DemoBox("col-4", value=120), span=4),
                    antd.Col(DemoBox("col-4", value=80), span=4),
                ],
                justify="space-around",
                align="middle",
            ),
            antd.Divider("Align Bottom", orientation="left"),
            antd.Row(
                [
                    antd.Col(DemoBox("col-4", value=100), span=4),
                    antd.Col(DemoBox("col-4", value=50), span=4),
                    antd.Col(DemoBox("col-4", value=120), span=4),
                    antd.Col(DemoBox("col-4", value=80), span=4),
                ],
                justify="space-between",
                align="bottom",
            ),
        ]
    )
