import render as r
import render_antd as antd


def app(_):
    time_picker = antd.TimePicker()
    r.autorun(lambda: print("changed", time_picker()))
    return time_picker
