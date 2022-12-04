import reflect_antd as antd


def app():
    gridStyle = {"width": "25%", "textAlign": "center"}
    return antd.Card(
        [
            antd.Card.Grid("Content", style=gridStyle),
            antd.Card.Grid("Content", hoverable=False, style=gridStyle),
            antd.Card.Grid("Content", style=gridStyle),
            antd.Card.Grid("Content", style=gridStyle),
            antd.Card.Grid("Content", style=gridStyle),
            antd.Card.Grid("Content", style=gridStyle),
            antd.Card.Grid("Content", style=gridStyle),
        ],
        title="Card Title",
    )
