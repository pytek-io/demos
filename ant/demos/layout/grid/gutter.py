from reflect_html import *
from reflect_antd import Row, Col, Divider

style = dict(background="#0092ff", padding="8px 0")


def app():
    return [
        Divider("Horizontal", orientation="left"),
        Row(
            [
                Col(div("col-6", style=style), className="gutter-row", span=6),
                Col(div("col-6", style=style), className="gutter-row", span=6),
                Col(div("col-6", style=style), className="gutter-row", span=6),
                Col(div("col-6", style=style), className="gutter-row", span=6),
            ],
            gutter=16,
        ),
        Divider("Responsive", orientation="left"),
        Row(
            [
                Col(div("col-6", style=style), className="gutter-row", span=6),
                Col(div("col-6", style=style), className="gutter-row", span=6),
                Col(div("col-6", style=style), className="gutter-row", span=6),
                Col(div("col-6", style=style), className="gutter-row", span=6),
            ],
            gutter=dict(xs=8, sm=16, md=24, lg=32),
        ),
        Divider("Vertical", orientation="left"),
        Row(
            [
                Col(div("col-6", style=style), className="gutter-row", span=6),
                Col(div("col-6", style=style), className="gutter-row", span=6),
                Col(div("col-6", style=style), className="gutter-row", span=6),
                Col(div("col-6", style=style), className="gutter-row", span=6),
                Col(div("col-6", style=style), className="gutter-row", span=6),
                Col(div("col-6", style=style), className="gutter-row", span=6),
                Col(div("col-6", style=style), className="gutter-row", span=6),
                Col(div("col-6", style=style), className="gutter-row", span=6),
            ],
            gutter=[16, 24],
        ),
    ]
