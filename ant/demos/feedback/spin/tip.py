from reflect_html import *
from reflect_antd import Spin, Alert


def app():
    return Spin(
        Alert(
            message="Alert message title",
            description="Further details about the context of this alert.",
            type="info",
        ),
        tip="Loading...",
    )
