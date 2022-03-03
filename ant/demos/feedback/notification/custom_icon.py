from reflect_html import *
from reflect_antd import Button, notification
from reflect_ant_icons import SmileOutlined


def app():
    def onClick():
        notification.open(
            {
                "message": "Notification Title",
                "description": "This is the content of the notification. This is the content of the notification. This is the content of the notification.",
                "icon": SmileOutlined(style={"color": "#108ee9"}),
            }
        )

    return Button("Open the notification box", type="primary", onClick=onClick)
