import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Space(
        [
            antd.Card(
                [html.p("Card content"), html.p("Card content")],
                title="Card",
                style=dict(width=300),
            ),
            antd.Card(
                [html.p("Card content"), html.p("Card content")],
                title="Card",
                style=dict(width=300),
            ),
        ],
        direction="vertical",
    )
