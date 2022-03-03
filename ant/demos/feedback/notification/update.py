from reflect_html import *
from reflect_antd import Button, notification
from reflect import schedule_callback


def openNotification():
    key = "updatable"
    notification.open(
        {
            "key": key,
            "message": "Notification Title",
            "description": "This description will update in one second.",
        }
    )
    schedule_callback(
        1,
        lambda: notification.open(
            {
                "key": key,
                "message": "New Title",
                "description": "New description",
            }
        ),
    )


def app():
    return Button("Open the notification box", type="primary", onClick=openNotification)
