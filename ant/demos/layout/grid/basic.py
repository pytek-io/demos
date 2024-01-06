import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Row(antd.Col("col", span=24)),
            antd.Row([antd.Col("col-12", span=12), antd.Col("col-12", span=12)]),
            antd.Row(
                [
                    antd.Col("col-8", span=8),
                    antd.Col("col-8", span=8),
                    antd.Col("col-8", span=8),
                ]
            ),
            antd.Row(
                [
                    antd.Col("col-6", span=6),
                    antd.Col("col-6", span=6),
                    antd.Col("col-6", span=6),
                    antd.Col("col-6", span=6),
                ]
            ),
        ]
    )
