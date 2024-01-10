import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Alert(
                message="Success Text",
                description="Success Description Success Description Success Description",
                type="success",
            ),
            antd.Alert(
                message="Info Text",
                description="Info Description Info Description Info Description Info Description",
                type="info",
            ),
            antd.Alert(
                message="Warning Text",
                description="Warning Description Warning Description Warning Description Warning Description",
                type="warning",
            ),
            antd.Alert(
                message="Error Text",
                description="Error Description Error Description Error Description Error Description",
                type="error",
            ),
        ]
    )
