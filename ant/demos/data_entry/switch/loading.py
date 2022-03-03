from reflect_html import *
from reflect_antd import Switch


def app():
    return [
        Switch(loading=True, defaultChecked=True),
        br(),
        Switch(size="small", loading=True),
    ]
