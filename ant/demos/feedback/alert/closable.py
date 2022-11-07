import reflect_antd as antd
import reflect_html as html

onClose = lambda: print("I have been closed.")


def app():
    return html.div(
        [
            antd.Alert(
                message="Warning Text Warning Text Warning TextW arning Text Warning Text Warning TextWarning Text",
                type="warning",
                closable=True,
                onClose=onClose,
            ),
            antd.Alert(
                message="Error Text",
                description="Error Description Error Description Error Description Error Description Error Description Error Description",
                type="error",
                closable=True,
                onClose=onClose,
            ),
        ]
    )
