from reflect_html import *
from reflect_antd import Row, Col


def app():
    return [
        Row([Col("col-8", span=8), Col("col-8", span=8, offset=8)]),
        Row(
            [
                Col("col-6 col-offset-6", span=6, offset=6),
                Col("col-6 col-offset-6", span=6, offset=6),
            ]
        ),
        Row(Col("col-12 col-offset-6", span=12, offset=6)),
    ]
