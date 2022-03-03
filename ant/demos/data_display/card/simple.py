from reflect_html import *
from reflect_antd import Card


def app():
    return Card(
        [p("Card content"), p("Card content"), p("Card content")], style=dict(width=300)
    )
