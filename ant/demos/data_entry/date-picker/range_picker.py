from reflect_html import *
from reflect_antd import DatePicker, Space

RangePicker = DatePicker.RangePicker


def app():
    return Space(
        [
            RangePicker(),
            RangePicker(showTime=True),
            RangePicker(picker="week"),
            RangePicker(picker="month"),
            RangePicker(picker="year"),
        ],
        direction="vertical",
        size=12,
    )
