import render_antd as antd
import render_html as html


def app(_):
    return antd.Card(
        [html.p("Card content"), html.p("Card content"), html.p("Card content")],
        style={"width": 300},
    )
