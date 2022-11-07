import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Switch(defaultChecked=True),
            html.br(),
            antd.Switch(size="small", defaultChecked=True),
        ]
    )
