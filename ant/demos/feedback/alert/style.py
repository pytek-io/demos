import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Alert(message="Success Text", type="success"),
            antd.Alert(message="Info Text", type="info"),
            antd.Alert(message="Warning Text", type="warning"),
            antd.Alert(message="Error Text", type="error"),
        ]
    )
