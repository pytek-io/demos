import reflect_antd as antd
import reflect_html as html


def app():
    def onClick():
        antd.notification.open(
            {
                "message": "Notification Title",
                "description": "This is the content of the notification. This is the content of the notification. This is the content of the notification.",
                "onClick": lambda: print("Notification Clicked!"),
            }
        )

    return antd.Button("Open the notification box", type="primary", onClick=onClick)
