import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Switch(loading=True, defaultChecked=True),
            html.br(),
            antd.Switch(size="small", loading=True),
        ]
    )
