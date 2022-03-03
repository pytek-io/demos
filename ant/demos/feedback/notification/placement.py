from reflect_html import *
from reflect_antd import Button, notification, Divider, Space
from reflect_ant_icons import (
    RadiusUpleftOutlined,
    RadiusUprightOutlined,
    RadiusBottomleftOutlined,
    RadiusBottomrightOutlined,
)


def app():
    def openNotification(placement):
        return lambda: notification.info(
            {
                "message": f"Notification {placement}",
                "description": "This is the content of the notification. This is the content of the notification. This is the content of the notification.",
                "placement": placement,
            }
        )

    return div(
        [
            Space(
                [
                    Button(
                        [RadiusUpleftOutlined(), "topLeft"],
                        type="primary",
                        onClick=openNotification("topLeft"),
                    ),
                    Button(
                        [RadiusUprightOutlined(), "topRight"],
                        type="primary",
                        onClick=openNotification("topRight"),
                    ),
                ]
            ),
            Divider(),
            Space(
                [
                    Button(
                        [RadiusBottomleftOutlined(), "bottomLeft"],
                        type="primary",
                        onClick=openNotification("bottomLeft"),
                    ),
                    Button(
                        [RadiusBottomrightOutlined(), "bottomRight"],
                        type="primary",
                        onClick=openNotification("bottomRight"),
                    ),
                ]
            ),
        ]
    )
