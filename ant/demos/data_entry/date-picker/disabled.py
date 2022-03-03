from reflect_html import *
from reflect_antd import DatePicker, Space
from datetime import datetime

RangePicker = DatePicker.RangePicker


def app():
    return Space(
        [
            DatePicker(defaultValue=datetime(2015, 6, 6), disabled=True),
            DatePicker(
                picker="month", defaultValue=datetime(2015, 6, 6), disabled=True
            ),
            RangePicker(
                defaultValue=[
                    datetime(2015, 6, 6),
                    datetime(2015, 6, 6),
                ],
                disabled=True,
            ),
            RangePicker(
                defaultValue=[
                    datetime(2019, 9, 3),
                    datetime(2019, 11, 22),
                ],
                disabled=[False, True],
            ),
        ],
        direction="vertical",
        size=12,
    )
