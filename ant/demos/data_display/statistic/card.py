from reflect_html import *
from reflect_antd import Statistic, Card, Row, Col
from reflect_ant_icons import ArrowUpOutlined, ArrowDownOutlined


def app():
    return div(
        Row(
            [
                Col(
                    Card(
                        Statistic(
                            title="Active",
                            value=11.28,
                            precision=2,
                            valueStyle=dict(color="#3f8600"),
                            prefix=ArrowUpOutlined([]),
                            suffix="%",
                        )
                    ),
                    span=12,
                ),
                Col(
                    Card(
                        Statistic(
                            title="Idle",
                            value=9.3,
                            precision=2,
                            valueStyle=dict(color="#cf1322"),
                            prefix=ArrowDownOutlined([]),
                            suffix="%",
                        )
                    ),
                    span=12,
                ),
            ],
            gutter=16,
        ),
        className="site-statistic-demo-card",
    )
