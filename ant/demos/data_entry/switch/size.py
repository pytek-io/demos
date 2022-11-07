from reflect_html import *
from reflect_antd import Switch


def app():
    return div(
        [
            Switch(defaultChecked=True),
            br(),
            Switch(size="small", defaultChecked=True),
        ]
    )
