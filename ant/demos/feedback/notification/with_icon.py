from reflect_html import *
from reflect_antd import Button, notification, Space, notification


def app():
    args = {
        "message": "Notification Title",
        "description": "This is the content of the notification. This is the content of the notification. This is the content of the notification.",
    }

    def openNotificationWithIcon(notification_type):
        return lambda: getattr(notification, notification_type)(args)

    return Space(
        [
            Button("Success", onClick=openNotificationWithIcon("success")),
            Button("Info", onClick=openNotificationWithIcon("info")),
            Button("Warning", onClick=openNotificationWithIcon("warning")),
            Button("Error", onClick=openNotificationWithIcon("error")),
        ]
    )
