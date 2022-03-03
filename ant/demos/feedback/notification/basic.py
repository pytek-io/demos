from reflect_html import *
from reflect_antd import Button, notification



def app():
    def onClick():
        notification.open(
            {
                "message": "Notification Title",
                "description": "This is the content of the notification. This is the content of the notification. This is the content of the notification.",
                "onClick": lambda: print("Notification Clicked!"),
            }
        )

    return Button("Open the notification box", type="primary", onClick=onClick)
