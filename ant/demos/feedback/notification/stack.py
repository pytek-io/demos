import render_antd as antd
import render_html as html
import render as r


def app(_):
    enabled = r.ObservableValue(True)
    threshold = r.ObservableValue(4)

    def openNotification():
        antd.notification.open(
            {
                "message": "Notification Title",
                "description": "This is the content of the notification.",
            }
        )

    return html.div(
        [
            antd.Space(
                [
                    html.div(
                        [
                            "Enabled: ",
                            antd.Switch(
                                value=enabled, onChange=lambda v: enabled.set(v)
                            ),
                        ],
                        style={"width": "100%"},
                    ),
                    html.div(
                        [
                            "Threshold: ",
                            antd.InputNumber(
                                disabled=lambda: not enabled(),
                                value=threshold,
                                step=1,
                                min=1,
                                max=10,
                            ),
                        ],
                        style={"width": "100%"},
                    ),
                ],
                size="large",
            ),
            antd.Divider(),
            antd.Button(
                "Open the notification box", type="primary", onClick=openNotification
            ),
        ]
    )
