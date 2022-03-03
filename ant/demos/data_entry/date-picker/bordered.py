from reflect_html import *
from reflect_antd import DatePicker, Space

RangePicker = DatePicker.RangePicker


def app():
    return Space(
        [
            DatePicker(bordered=False),
            DatePicker(picker="week", bordered=False),
            DatePicker(picker="month", bordered=False),
            DatePicker(picker="year", bordered=False),
            RangePicker(bordered=False),
            RangePicker(picker="week", bordered=False),
            RangePicker(picker="month", bordered=False),
            RangePicker(picker="year", bordered=False),
        ],
        direction="vertical",
        size=12,
    )
