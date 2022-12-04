import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        antd.Row(
            [
                antd.Col(
                    antd.Card("Card content", title="Card title", bordered=False),
                    span=8,
                ),
                antd.Col(
                    antd.Card("Card content", title="Card title", bordered=False),
                    span=8,
                ),
                antd.Col(
                    antd.Card("Card content", title="Card title", bordered=False),
                    span=8,
                ),
            ],
            gutter=16,
        ),
        className="site-card-wrapper",
    )
