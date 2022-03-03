from reflect_html import *
from reflect_antd import Statistic, Row, Col, Button


def app():
    return Row(
        [
            Col(Statistic(title="Active Users", value=112893), span=12),
            Col(
                [
                    Statistic(title="Account Balance (CNY)", value=112893, precision=2),
                    Button("Recharge", style=dict(marginTop=16), type="primary"),
                ],
                span=12,
            ),
            Col(Statistic(title="Active Users", value=112893, loading=True), span=12),
        ],
        gutter=16,
    )
