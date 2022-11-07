from reflect_html import *
from reflect_antd import TimePicker

RangePicker = TimePicker.RangePicker


def app():
    return div(
        [
            TimePicker(bordered=False),
            RangePicker(bordered=False),
        ]
    )
