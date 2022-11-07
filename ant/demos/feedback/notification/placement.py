import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    def openNotification(placement):
        return lambda: antd.notification.info(
            {
                "message": f"Notification {placement}",
                "description": "This is the content of the notification. This is the content of the notification. This is the content of the notification.",
                "placement": placement,
            }
        )

    return html.div(
        [
            antd.Space(
                [
                    antd.Button(
                        [ant_icons.RadiusUpleftOutlined(), "topLeft"],
                        type="primary",
                        onClick=openNotification("topLeft"),
                    ),
                    antd.Button(
                        [ant_icons.RadiusUprightOutlined(), "topRight"],
                        type="primary",
                        onClick=openNotification("topRight"),
                    ),
                ]
            ),
            antd.Divider(),
            antd.Space(
                [
                    antd.Button(
                        [ant_icons.RadiusBottomleftOutlined(), "bottomLeft"],
                        type="primary",
                        onClick=openNotification("bottomLeft"),
                    ),
                    antd.Button(
                        [ant_icons.RadiusBottomrightOutlined(), "bottomRight"],
                        type="primary",
                        onClick=openNotification("bottomRight"),
                    ),
                ]
            ),
        ]
    )
