import render_antd as antd
import render_html as html


def app(_):
    def onClick():
        antd.notification.open(
            {
                "message": "Notification Title",
                "description": "This is the content of the notification. This is the content of the notification. This is the content of the notification.",
                "onClick": lambda: print("Notification Clicked!"),
            }
        )

    return antd.Button("Open the notification box", type="primary", onClick=onClick)
