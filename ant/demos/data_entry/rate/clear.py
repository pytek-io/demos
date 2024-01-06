import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Rate(defaultValue=3),
            html.span("allowClear: true", className="ant-rate-text"),
            html.br(),
            antd.Rate(allowClear=False, defaultValue=3),
            html.span("allowClear: false", className="ant-rate-text"),
        ]
    )
