import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Divider("Normal", orientation="left"),
            antd.Row(
                [
                    antd.Col("1 col-order-4", span=6, order=4),
                    antd.Col("2 col-order-3", span=6, order=3),
                    antd.Col("3 col-order-2", span=6, order=2),
                    antd.Col("4 col-order-1", span=6, order=1),
                ]
            ),
            antd.Divider("Responsive", orientation="left"),
            antd.Row(
                [
                    antd.Col(
                        "1 col-order-responsive",
                        span=6,
                        xs={"order": 1},
                        sm={"order": 2},
                        md={"order": 3},
                        lg={"order": 4},
                    ),
                    antd.Col(
                        "2 col-order-responsive",
                        span=6,
                        xs={"order": 2},
                        sm={"order": 1},
                        md={"order": 4},
                        lg={"order": 3},
                    ),
                    antd.Col(
                        "3 col-order-responsive",
                        span=6,
                        xs={"order": 3},
                        sm={"order": 4},
                        md={"order": 2},
                        lg={"order": 1},
                    ),
                    antd.Col(
                        "4 col-order-responsive",
                        span=6,
                        xs={"order": 4},
                        sm={"order": 3},
                        md={"order": 1},
                        lg={"order": 2},
                    ),
                ]
            ),
        ]
    )
