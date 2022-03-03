from reflect_html import *
from reflect_antd import Rate
from reflect import js


def app():
    return div(
        [
            Rate(defaultValue=2, character=js("index_plus_one")),
            br(),
            Rate(defaultValue=3, character=js("custom_icons")),
        ]
    )
