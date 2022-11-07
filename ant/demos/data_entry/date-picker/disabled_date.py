import datetime

import reflect as r
import reflect_antd as antd
import reflect_html as html

RangePicker = antd.DatePicker.RangePicker
JS_MODULES = ["ant_demo"]


def app():
    disabledDate = r.js("datePickerDisableDate")
    disabledDateTime = r.js("datePickerDisableDateTime")
    disabledRangeTime = r.js("datePickerDisableRangeTime")
    return antd.Space(
        [
            antd.DatePicker(
                format="YYYY-MM-DD HH:mm:ss",
                disabledDate=disabledDate,
                disabledTime=disabledDateTime,
                showTime=dict(defaultValue=datetime.datetime.now()),
            ),
            antd.DatePicker(picker="month", disabledDate=disabledDate),
            RangePicker(disabledDate=disabledDate),
            RangePicker(
                disabledDate=disabledDate,
                disabledTime=disabledRangeTime,
                showTime=dict(
                    hideDisabledOptions=True,
                    defaultValue=[
                        datetime.datetime.now(),
                        datetime.datetime.now() + datetime.timedelta(hours=12),
                    ],
                ),
                format="YYYY-MM-DD HH:mm:ss",
            ),
        ],
        direction="vertical",
        size=12,
    )
