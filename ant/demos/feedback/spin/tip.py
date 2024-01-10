import render_antd as antd
import render_html as html


def app(_):
    return antd.Spin(
        antd.Alert(
            message="Alert message title",
            description="Further details about the context of this alert.",
            type="info",
        ),
        tip="Loading...",
    )
