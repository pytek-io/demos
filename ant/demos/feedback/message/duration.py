from reflect_html import *
from reflect_antd import message, Button


def success():
    message.success(
        "This is a prompt message for success, and it will disappear in 10 seconds", 10
    )


def app():
    return Button("Customized display duration", onClick=success)
