import datetime

import reflect_antd as antd

RangePicker = antd.DatePicker.RangePicker


def app():
    return antd.Space([RangePicker()], direction="vertical", size=12)
