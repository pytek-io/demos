import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Pagination(simple=True, defaultCurrent=2, total=50),
            html.br(),
            antd.Pagination(disabled=True, simple=True, defaultCurrent=2, total=50),
        ]
    )
