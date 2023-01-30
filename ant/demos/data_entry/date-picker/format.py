import datetime

import reflect as r
import reflect_antd as antd

RangePicker = antd.DatePicker.RangePicker
dateFormat = "YYYY/MM/DD"
monthFormat = "YYYY/MM"
dateFormatList = ["DD/MM/YYYY", "DD/MM/YY"]


datePickerFormatter = r.JSMethod(
    "datePickerFormatter",
    f"""return `custom format: ${{value.format('{dateFormat}')}}`""",
    "value",
)


def app():
    defaultValue = datetime.datetime(2015, 1, 1)
    return antd.Space(
        [
            antd.DatePicker(defaultValue=defaultValue, format=dateFormat),
            antd.DatePicker(defaultValue=defaultValue, format=dateFormatList),
            antd.DatePicker(
                defaultValue=defaultValue, format=monthFormat, picker="month"
            ),
            RangePicker(defaultValue=[defaultValue, defaultValue], format=dateFormat),
            antd.DatePicker(defaultValue=defaultValue, format=datePickerFormatter),
        ],
        direction="vertical",
        size=12,
    )
