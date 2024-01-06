import datetime

import render_antd as antd
import render_html as html


def app():
    return antd.TimePicker(defaultValue=datetime.time(12, 8, 23), disabled=True)
