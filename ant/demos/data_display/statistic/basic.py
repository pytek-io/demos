import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Row(
        [
            antd.Col(antd.Statistic(title="Active Users", value=112893), span=12),
            antd.Col(
                [
                    antd.Statistic(
                        title="Account Balance (CNY)", value=112893, precision=2
                    ),
                    antd.Button("Recharge", style=dict(marginTop=16), type="primary"),
                ],
                span=12,
            ),
            antd.Col(
                antd.Statistic(title="Active Users", value=112893, loading=True),
                span=12,
            ),
        ],
        gutter=16,
    )
