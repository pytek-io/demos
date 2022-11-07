import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Alert(message="Success Text", type="success"),
            antd.Alert(message="Info Text", type="info"),
            antd.Alert(message="Warning Text", type="warning"),
            antd.Alert(message="Error Text", type="error"),
        ]
    )
