from reflect_html import *
from reflect_antd import Space, Card


def app():
    return  Space(
            [
                Card(
                    [p("Card content"), p("Card content")],
                    title="Card",
                    style=dict(width=300),
                ),
                Card(
                    [p("Card content"), p("Card content")],
                    title="Card",
                    style=dict(width=300),
                ),
            ],
            direction="vertical",
        )
