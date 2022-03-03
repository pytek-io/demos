from reflect_html import *
from reflect_antd import Checkbox, Row, Col

from reflect import autorun


def app():

    check_box_group = Checkbox.Group(
        Row(
            [
                Col(Checkbox("A", key="A"), span=8),
                Col(Checkbox("B", key="B"), span=8),
                Col(Checkbox("C", key="C"), span=8),
                Col(Checkbox("D", key="D"), span=8),
                Col(Checkbox("E", key="E"), span=8),
            ]
        ),
        style=dict(width="100%"),
    )
    autorun(lambda: print("checked = ", check_box_group()))
    return check_box_group
