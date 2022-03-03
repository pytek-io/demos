from reflect_html import *
from reflect_antd import Button, notification
from datetime import datetime


def app():
    key = str(datetime.now())
    btn = Button(
        "Confirm", type="primary", size="small", onClick=lambda: notification.close(key)
    )

    def onClick():
        notification.open(
            {
                "message": "Notification Title",
                "description": 'Press confirm to close this popup window.',
                "btn": btn,
                "key": key,
                # "onClose": close,
            },
            0
        )

    return Button("Open the notification box", type="primary", onClick=onClick)
