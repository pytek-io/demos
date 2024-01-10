import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Checkbox(defaultChecked=False, disabled=True),
            html.br(),
            antd.Checkbox(defaultChecked=True, disabled=True),
        ]
    )
