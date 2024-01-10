import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Button("Primary Button", type="primary"),
            antd.Button("Default Button"),
            antd.Button("Dashed Button", type="dashed"),
            html.br(),
            antd.Button("Text Button", type="text"),
            antd.Button("Link Button", type="link"),
        ]
    )
