import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Alert(message="Warning text", banner=True),
            html.br(),
            antd.Alert(
                message="Very long warning text warning text text text text text text text",
                banner=True,
                closable=True,
            ),
            html.br(),
            antd.Alert(
                showIcon=False, message="Warning text without icon", banner=True
            ),
            html.br(),
            antd.Alert(type="error", message="Error text", banner=True),
        ]
    )
