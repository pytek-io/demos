from reflect_html import *
from reflect_antd import Row, Col, Divider


def app():
    return div([
        Divider("sub-element align left", orientation="left"),
        Row(
            [
                Col("col-4", span=4),
                Col("col-4", span=4),
                Col("col-4", span=4),
                Col("col-4", span=4),
            ],
            justify="start",
        ),
        Divider("sub-element align center", orientation="left"),
        Row(
            [
                Col("col-4", span=4),
                Col("col-4", span=4),
                Col("col-4", span=4),
                Col("col-4", span=4),
            ],
            justify="center",
        ),
        Divider("sub-element align right", orientation="left"),
        Row(
            [
                Col("col-4", span=4),
                Col("col-4", span=4),
                Col("col-4", span=4),
                Col("col-4", span=4),
            ],
            justify="end",
        ),
        Divider("sub-element monospaced arrangement", orientation="left"),
        Row(
            [
                Col("col-4", span=4),
                Col("col-4", span=4),
                Col("col-4", span=4),
                Col("col-4", span=4),
            ],
            justify="space-between",
        ),
        Divider("sub-element align full", orientation="left"),
        Row(
            [
                Col("col-4", span=4),
                Col("col-4", span=4),
                Col("col-4", span=4),
                Col("col-4", span=4),
            ],
            justify="space-around",
        ),
    ]
)