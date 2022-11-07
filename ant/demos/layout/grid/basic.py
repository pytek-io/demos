from reflect_html import *
from reflect_antd import Row, Col


def app():
    return div(
        [
            Row(Col("col", span=24)),
            Row([Col("col-12", span=12), Col("col-12", span=12)]),
            Row([Col("col-8", span=8), Col("col-8", span=8), Col("col-8", span=8)]),
            Row(
                [
                    Col("col-6", span=6),
                    Col("col-6", span=6),
                    Col("col-6", span=6),
                    Col("col-6", span=6),
                ]
            ),
        ]
    )
