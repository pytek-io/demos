from reflect_html import *
from reflect_antd import Row, Col


def app():
    return Row(
        [
            Col("col-18 col-push-6", span=18, push=6),
            Col("col-6 col-pull-18", span=6, pull=18),
        ]
    )
