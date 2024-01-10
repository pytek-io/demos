import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Alert(message="Success Tips", type="success", showIcon=True),
            antd.Alert(message="Informational Notes", type="info", showIcon=True),
            antd.Alert(message="Warning", type="warning", showIcon=True, closable=True),
            antd.Alert(message="Error", type="error", showIcon=True),
            antd.Alert(
                message="Success Tips",
                description="Detailed description and advice about successful copywriting.",
                type="success",
                showIcon=True,
            ),
            antd.Alert(
                message="Informational Notes",
                description="Additional description and information about copywriting.",
                type="info",
                showIcon=True,
            ),
            antd.Alert(
                message="Warning",
                description="This is a warning notice about copywriting.",
                type="warning",
                showIcon=True,
                closable=True,
            ),
            antd.Alert(
                message="Error",
                description="This is an error message about copywriting.",
                type="error",
                showIcon=True,
            ),
        ]
    )
