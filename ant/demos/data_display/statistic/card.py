import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        antd.Row(
            [
                antd.Col(
                    antd.Card(
                        antd.Statistic(
                            title="Active",
                            value=11.28,
                            precision=2,
                            valueStyle=dict(color="#3f8600"),
                            prefix=ant_icons.ArrowUpOutlined([]),
                            suffix="%",
                        )
                    ),
                    span=12,
                ),
                antd.Col(
                    antd.Card(
                        antd.Statistic(
                            title="Idle",
                            value=9.3,
                            precision=2,
                            valueStyle=dict(color="#cf1322"),
                            prefix=ant_icons.ArrowDownOutlined([]),
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
