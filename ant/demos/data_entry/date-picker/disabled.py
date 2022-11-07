import datetime

import reflect_antd as antd
import reflect_html as html

RangePicker = antd.DatePicker.RangePicker


def app():
    return antd.Space(
        [
            antd.DatePicker(defaultValue=datetime.datetime(2015, 6, 6), disabled=True),
            antd.DatePicker(
                picker="month",
                defaultValue=datetime.datetime(2015, 6, 6),
                disabled=True,
            ),
            RangePicker(
                defaultValue=[
                    datetime.datetime(2015, 6, 6),
                    datetime.datetime(2015, 6, 6),
                ],
                disabled=True,
            ),
            RangePicker(
                defaultValue=[
                    datetime.datetime(2019, 9, 3),
                    datetime.datetime(2019, 11, 22),
                ],
                disabled=[False, True],
            ),
        ],
        direction="vertical",
        size=12,
    )
