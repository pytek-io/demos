from reflect_html import *
from reflect_antd import message, Button


def success():
    message.success(
        {
            "content": "This is a prompt message with custom className and style",
            "className": "custom-class",
            "style": {
                "marginTop": "20vh",
            },
        }
    )


def app():
    return Button("Customized style", onClick=success)
