from reflect_html import *
from reflect_antd import Card


def app():
    gridStyle = {
        "width": "25%",
        "textAlign": "center",
    }
    return Card(
        [
            Card.Grid("Content", style=gridStyle),
            Card.Grid("Content", hoverable=False, style=gridStyle),
            Card.Grid("Content", style=gridStyle),
            Card.Grid("Content", style=gridStyle),
            Card.Grid("Content", style=gridStyle),
            Card.Grid("Content", style=gridStyle),
            Card.Grid("Content", style=gridStyle),
        ],
        title="Card Title",
    )
