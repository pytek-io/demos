import datetime

import render_antd as antd
import render_html as html


def app(_):
    key = str(datetime.datetime.now())
    btn = antd.Button(
        "Confirm",
        type="primary",
        size="small",
        onClick=lambda: antd.notification.destroy(key),
    )

    def onClick():
        antd.notification.open(
            {
                "message": "Notification Title",
                "description": "Press confirm to close this popup window.",
                "btn": btn,
                "key": key,
            },
            0,
        )

    return antd.Button("Open the notification box", type="primary", onClick=onClick)
