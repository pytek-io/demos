from reflect_html import *
from reflect_antd import Card


def app():
    return div(
        Card(
            [p("Card content"), p("Card content"), p("Card content")],
            title="Card title",
            bordered=False,
            style=dict(width=300),
        ),
        className="site-card-border-less-wrapper",
    )
