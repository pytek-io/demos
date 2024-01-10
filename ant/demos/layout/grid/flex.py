import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Divider("sub-element align left", orientation="left"),
            antd.Row(
                [
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                ],
                justify="start",
            ),
            antd.Divider("sub-element align center", orientation="left"),
            antd.Row(
                [
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                ],
                justify="center",
            ),
            antd.Divider("sub-element align right", orientation="left"),
            antd.Row(
                [
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                ],
                justify="end",
            ),
            antd.Divider("sub-element monospaced arrangement", orientation="left"),
            antd.Row(
                [
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                ],
                justify="space-between",
            ),
            antd.Divider("sub-element align full", orientation="left"),
            antd.Row(
                [
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                    antd.Col("col-4", span=4),
                ],
                justify="space-around",
            ),
        ]
    )
