from reflect_html import *
from reflect_antd import Card, Col, Row


def app():
    return div(
        Row(
            [
                Col(Card("Card content", title="Card title", bordered=False), span=8),
                Col(Card("Card content", title="Card title", bordered=False), span=8),
                Col(Card("Card content", title="Card title", bordered=False), span=8),
            ],
            gutter=16,
        ),
        className="site-card-wrapper",
    )
