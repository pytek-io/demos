import datetime

import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.TimePicker(defaultValue=datetime.time(12, 8, 23), size="large"),
            antd.TimePicker(defaultValue=datetime.time(12, 8, 23)),
            antd.TimePicker(defaultValue=datetime.time(12, 8, 23), size="small"),
        ]
    )
