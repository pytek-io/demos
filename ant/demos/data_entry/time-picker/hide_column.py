import datetime

import render_antd as antd
import render_html as html


def app(_):
    return antd.TimePicker(defaultValue=datetime.time(12, 8, 0), format="HH:mm")
