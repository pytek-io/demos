import render as r
import render_antd as antd
import render_html as html


def app():
    def onClick():
        antd.notification.open(
            {
                "message": "Notification Title",
                "description": "I will never close automatically. This is a purposely very very long description that has many many characters and words.",
                "duration": 0,
            }
        )

    return antd.Button("Open the notification box", type="primary", onClick=onClick)
