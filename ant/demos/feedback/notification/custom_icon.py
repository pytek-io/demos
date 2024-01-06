import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app():
    def onClick():
        antd.notification.open(
            {
                "message": "Notification Title",
                "description": "This is the content of the notification. This is the content of the notification. This is the content of the notification.",
                "icon": ant_icons.SmileOutlined(style={"color": "#108ee9"}),
            }
        )

    return antd.Button("Open the notification box", type="primary", onClick=onClick)
