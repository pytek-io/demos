from reflect_html import *
from reflect_antd import DatePicker, Space
from reflect import js
from datetime import datetime

RangePicker = DatePicker.RangePicker

dateFormat = "YYYY/MM/DD"
monthFormat = "YYYY/MM"
dateFormatList = ["DD/MM/YYYY", "DD/MM/YY"]

JS_MODULES = ["ant_demo"]

def app():
    defaultValue = datetime(2015, 1, 1)
    return Space(
        [
            DatePicker(defaultValue=defaultValue, format=dateFormat),
            DatePicker(
                defaultValue=defaultValue,
                format=dateFormatList,
            ),
            DatePicker(
                defaultValue=defaultValue,
                format=monthFormat,
                picker="month",
            ),
            RangePicker(
                defaultValue=[
                    defaultValue,
                    defaultValue,
                ],
                format=dateFormat,
            ),
            DatePicker(
                defaultValue=defaultValue, format=js("datePickerFormatter")
            ),
        ],
        direction="vertical",
        size=12,
    )
