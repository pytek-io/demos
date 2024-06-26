import render as r
import render_antd as antd


def openNotification():
    key = "updatable"
    antd.notification.open(
        {
            "key": key,
            "message": "Notification Title",
            "description": "This description will update in one second.",
        }
    )
    r.schedule_callback(
        1,
        lambda: antd.notification.open(
            {"key": key, "message": "New Title", "description": "New description"}
        ),
    )


def app(_):
    return antd.Button(
        "Open the notification box", type="primary", onClick=openNotification
    )
