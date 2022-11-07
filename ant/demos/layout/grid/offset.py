import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Row([antd.Col("col-8", span=8), antd.Col("col-8", span=8, offset=8)]),
            antd.Row(
                [
                    antd.Col("col-6 col-offset-6", span=6, offset=6),
                    antd.Col("col-6 col-offset-6", span=6, offset=6),
                ]
            ),
            antd.Row(antd.Col("col-12 col-offset-6", span=12, offset=6)),
        ]
    )
