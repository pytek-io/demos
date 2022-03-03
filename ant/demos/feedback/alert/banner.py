from reflect_html import *
from reflect_antd import Alert


def app():
    return [
        Alert(message="Warning text", banner=True),
        br(),
        Alert(
            message="Very long warning text warning text text text text text text text",
            banner=True,
            closable=True,
        ),
        br(),
        Alert(showIcon=False, message="Warning text without icon", banner=True),
        br(),
        Alert(type="error", message="Error text", banner=True),
    ]
