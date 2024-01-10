import datetime

import render as r
import render_antd as antd

RangePicker = antd.DatePicker.RangePicker
dateFormat = "YYYY/MM/DD"
monthFormat = "YYYY/MM"
dateFormatList = ["DD/MM/YYYY", "DD/MM/YY"]


custom_date_formatter = r.js_arrow(
    "custom_date_formatter",
    f"value => `custom format: ${{value.format('{dateFormat}')}}`",
)


def app(_):
    defaultValue = datetime.datetime(2015, 1, 1)
    return antd.Space(
        [
            antd.DatePicker(defaultValue=defaultValue, format=dateFormat),
            antd.DatePicker(defaultValue=defaultValue, format=dateFormatList),
            antd.DatePicker(
                defaultValue=defaultValue, format=monthFormat, picker="month"
            ),
            RangePicker(defaultValue=[defaultValue, defaultValue], format=dateFormat),
            antd.DatePicker(defaultValue=defaultValue, format=custom_date_formatter),
        ],
        direction="vertical",
        size=12,
    )
