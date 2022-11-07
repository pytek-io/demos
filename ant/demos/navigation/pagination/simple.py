import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Pagination(simple=True, defaultCurrent=2, total=50),
            html.br(),
            antd.Pagination(disabled=True, simple=True, defaultCurrent=2, total=50),
        ]
    )
