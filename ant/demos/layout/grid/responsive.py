from reflect_html import *
from reflect_antd import Row, Col


def app():
    return Row(
        [
            Col("Col", xs=2, sm=4, md=6, lg=8, xl=10),
            Col("Col", xs=20, sm=16, md=12, lg=8, xl=4),
            Col("Col", xs=2, sm=4, md=6, lg=8, xl=10),
        ]
    )
