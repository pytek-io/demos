import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Progress(percent=50, steps=3),
            html.br(),
            antd.Progress(percent=30, steps=5),
            html.br(),
            antd.Progress(percent=100, steps=5, size="small", strokeColor="#52c41a"),
        ]
    )
