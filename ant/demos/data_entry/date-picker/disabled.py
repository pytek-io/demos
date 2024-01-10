import datetime

import render_antd as antd

RangePicker = antd.DatePicker.RangePicker


def app(_):
    return antd.Space([RangePicker()], direction="vertical", size=12)
