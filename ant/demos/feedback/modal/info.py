from reflect_html import *
from reflect_antd import Modal, Button, Space


def info():
    print("calling info")
    Modal.info(
        {
            "title": "This is a notification message",
            "content": div(
                [
                    p("some messages...some messages..."),
                    p("some messages...some messages..."),
                ]
            ),
        }
    )


def success():
    Modal.success(
        {
            "content": "some messages...some messages...",
        }
    )


def error():
    Modal.error(
        {
            "title": "This is an error message",
            "content": "some messages...some messages...",
        }
    )


def warning():
    Modal.warning(
        {
            "title": "This is a warning message",
            "content": "some messages...some messages...",
        }
    )


def app():
    return Space(
        [
            Button("Info", onClick=info),
            Button("Success", onClick=success),
            Button("Error", onClick=error),
            Button("Warning", onClick=warning),
        ]
    )
