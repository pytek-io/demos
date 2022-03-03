from reflect_html import *
from reflect_antd import Row, Col


def app():
    return Row(
        [
            Col("Col", xs=dict(span=5, offset=1), lg=dict(span=6, offset=2)),
            Col("Col", xs=dict(span=11, offset=1), lg=dict(span=6, offset=2)),
            Col("Col", xs=dict(span=5, offset=1), lg=dict(span=6, offset=2)),
        ]
    )
