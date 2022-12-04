import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Card(
        [html.p("Card content"), html.p("Card content"), html.p("Card content")],
        style=dict(width=300),
    )
