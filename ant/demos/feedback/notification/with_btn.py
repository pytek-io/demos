import datetime

import reflect_antd as antd
import reflect_html as html


def app():
    key = str(datetime.datetime.now())
    btn = antd.Button(
        "Confirm",
        type="primary",
        size="small",
        onClick=lambda: antd.notification.close(key),
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
