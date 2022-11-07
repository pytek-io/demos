import reflect_antd as antd
import reflect_html as html


def app():
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
