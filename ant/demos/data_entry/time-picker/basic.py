import datetime

import render as r
import render_antd as antd
import render_html as html


def app():
    time_picker = antd.TimePicker()
    r.autorun(lambda: print("changed", time_picker()))
    return time_picker
