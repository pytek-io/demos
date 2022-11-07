import datetime

import reflect_antd as antd
import reflect_html as html


def app():
    return antd.TimePicker(defaultValue=datetime.time(12, 8, 0), format="HH:mm")
