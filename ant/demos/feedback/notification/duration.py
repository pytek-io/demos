from reflect_html import *
from reflect_antd import Button, notification
from reflect import schedule_callback


def app():
    def onClick():
        notification.open(
            {
                "message": "Notification Title",
                "description": "I will never close automatically. This is a purposely very very long description that has many many characters and words.",
                "duration": 0,
            }
        )

    return Button("Open the notification box", type="primary", onClick=onClick)
