from reflect_html import *
from reflect_antd import DatePicker, Space
from reflect import js
from datetime import datetime, timedelta
RangePicker = DatePicker.RangePicker

JS_MODULES = ["ant_demo"]

def app():
    disabledDate = js("datePickerDisableDate")
    disabledDateTime = js("datePickerDisableDateTime")
    disabledRangeTime = js("datePickerDisableRangeTime")
    return Space(
        [
            DatePicker(
                format="YYYY-MM-DD HH:mm:ss",
                disabledDate=disabledDate,
                disabledTime=disabledDateTime,
                showTime=dict(defaultValue=datetime.now()),
            ),
            DatePicker(picker="month", disabledDate=disabledDate),
            RangePicker(disabledDate=disabledDate),
            RangePicker(
                disabledDate=disabledDate,
                disabledTime=disabledRangeTime,
                showTime=dict(
                    hideDisabledOptions=True,
                    defaultValue=[
                        datetime.now(),
                        datetime.now() + timedelta(hours=12),
                    ],
                ),
                format="YYYY-MM-DD HH:mm:ss",
            ),
        ],
        direction="vertical",
        size=12,
    )
