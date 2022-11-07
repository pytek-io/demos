import reflect_antd as antd
import reflect_html as html


def app():
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
                        xs=dict(order=1),
                        sm=dict(order=2),
                        md=dict(order=3),
                        lg=dict(order=4),
                    ),
                    antd.Col(
                        "2 col-order-responsive",
                        span=6,
                        xs=dict(order=2),
                        sm=dict(order=1),
                        md=dict(order=4),
                        lg=dict(order=3),
                    ),
                    antd.Col(
                        "3 col-order-responsive",
                        span=6,
                        xs=dict(order=3),
                        sm=dict(order=4),
                        md=dict(order=2),
                        lg=dict(order=1),
                    ),
                    antd.Col(
                        "4 col-order-responsive",
                        span=6,
                        xs=dict(order=4),
                        sm=dict(order=3),
                        md=dict(order=1),
                        lg=dict(order=2),
                    ),
                ]
            ),
        ]
    )
