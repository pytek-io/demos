import render_antd as antd
import render_html as html


def app():
    return html.div(
        antd.Card(
            [html.p("Card content"), html.p("Card content"), html.p("Card content")],
            title="Card title",
            bordered=False,
            style={"width": 300},
        ),
        className="site-card-border-less-wrapper",
    )
