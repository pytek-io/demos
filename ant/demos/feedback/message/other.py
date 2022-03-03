from reflect_html import *
from reflect_antd import message, Button, Space


def success():
    message.success("This is a success message")


def error():
    message.error("This is an error message")


def warning():
    message.warning("This is a warning message")


def app():
    return Space(
        [
            Button("Success", onClick=success),
            Button("Error", onClick=error),
            Button("Warning", onClick=warning),
        ]
    )
