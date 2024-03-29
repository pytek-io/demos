import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Alert(
                message="Warning Text",
                type="warning",
                description="Warning Description",
                closable=True,
                onClose=lambda: print("Warning has been closed."),
            ),
            antd.Alert(
                message="Error Text",
                type="error",
                description="Error Description",
                closable=True,
                onClose=lambda: print("Error has been closed."),
            ),
        ]
    )
