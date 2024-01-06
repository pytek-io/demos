import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Card("More", title="Default size card", extra=html.a(href=True)),
            html.p("Card content"),
            html.p("Card content"),
            html.p("Card content"),
            antd.Card(
                "More", size="small", title="Small size card", extra=html.a(href=True)
            ),
            html.p("Card content"),
            html.p("Card content"),
            html.p("Card content"),
        ]
    )
