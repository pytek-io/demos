import render_antd as antd
import render_html as html


def app(_):
    return antd.Space(
        [
            antd.Card(
                [html.p("Card content"), html.p("Card content")],
                title="Card",
                style={"width": 300},
            ),
            antd.Card(
                [html.p("Card content"), html.p("Card content")],
                title="Card",
                style={"width": 300},
            ),
        ],
        direction="vertical",
    )
