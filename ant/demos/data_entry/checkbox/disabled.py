import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Checkbox(defaultChecked=False, disabled=True),
            html.br(),
            antd.Checkbox(defaultChecked=True, disabled=True),
        ]
    )
