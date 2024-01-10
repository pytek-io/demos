import datetime

import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.TimePicker(defaultValue=datetime.time(12, 8, 23), size="large"),
            antd.TimePicker(defaultValue=datetime.time(12, 8, 23)),
            antd.TimePicker(defaultValue=datetime.time(12, 8, 23), size="small"),
        ]
    )
