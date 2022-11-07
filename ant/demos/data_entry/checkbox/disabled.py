from reflect_html import *
from reflect_antd import Checkbox


def app():
    return div(
        [
            Checkbox(defaultChecked=False, disabled=True),
            br(),
            Checkbox(defaultChecked=True, disabled=True),
        ]
    )
