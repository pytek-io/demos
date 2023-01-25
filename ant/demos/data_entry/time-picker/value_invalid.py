# this example is not relevant for reflect

import datetime

import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    time_picker = antd.TimePicker(defaultValue=datetime.time(0, 0, 0))
    r.autorun(lambda: print(time_picker()))
    return time_picker