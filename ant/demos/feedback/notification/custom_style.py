import render_antd as antd
import render_html as html


def app():
    def onClick():
        antd.notification.open(
            {
                "message": "Notification Title",
                "description": "This is the content of the notification. This is the content of the notification. This is the content of the notification.",
                "className": "custom-class",
                "style": {"width": 600},
            }
        )

    return antd.Button("Open the notification box", type="primary", onClick=onClick)
