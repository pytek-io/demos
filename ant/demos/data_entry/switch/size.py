import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Switch(defaultChecked=True),
            html.br(),
            antd.Switch(size="small", defaultChecked=True),
        ]
    )
