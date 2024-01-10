import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Badge(status="success"),
            antd.Badge(status="error"),
            antd.Badge(status="default"),
            antd.Badge(status="processing"),
            antd.Badge(status="warning"),
            html.br(),
            antd.Badge(status="success", text="Success"),
            html.br(),
            antd.Badge(status="error", text="Error"),
            html.br(),
            antd.Badge(status="default", text="Default"),
            html.br(),
            antd.Badge(status="processing", text="Processing"),
            html.br(),
            antd.Badge(status="warning", text="Warning"),
        ]
    )
