import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Spin(
        antd.Alert(
            message="Alert message title",
            description="Further details about the context of this alert.",
            type="info",
        ),
        tip="Loading...",
    )
