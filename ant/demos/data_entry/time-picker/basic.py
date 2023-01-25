import datetime

import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    time_picker = antd.TimePicker()
    r.autorun(lambda: print("changed", time_picker()))
    return time_picker
