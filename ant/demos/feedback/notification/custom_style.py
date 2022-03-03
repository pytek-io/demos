from reflect_html import *
from reflect_antd import Button, notification


def app():
    def onClick():
        notification.open(
            {
                "message": "Notification Title",
                "description": "This is the content of the notification. This is the content of the notification. This is the content of the notification.",
                "className": "custom-class",
                "style": {
                    "width": 600,
                },
            },
        )

    return Button("Open the notification box", type="primary", onClick=onClick)
