import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Rate(defaultValue=2, character=r.js("index_plus_one")),
            html.br(),
            antd.Rate(defaultValue=3, character=r.js("custom_icons")),
        ]
    )
