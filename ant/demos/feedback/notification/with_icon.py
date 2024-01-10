import render_antd as antd
import render_html as html


def app(_):
    args = {
        "message": "Notification Title",
        "description": "This is the content of the notification. This is the content of the notification. This is the content of the notification.",
    }

    def openNotificationWithIcon(notification_type):
        return lambda: getattr(antd.notification, notification_type)(args)

    return antd.Space(
        [
            antd.Button("Success", onClick=openNotificationWithIcon("success")),
            antd.Button("Info", onClick=openNotificationWithIcon("info")),
            antd.Button("Warning", onClick=openNotificationWithIcon("warning")),
            antd.Button("Error", onClick=openNotificationWithIcon("error")),
        ]
    )
