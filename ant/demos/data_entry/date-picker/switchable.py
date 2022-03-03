from reflect_html import *
from reflect_antd import DatePicker, TimePicker, Select, Space

from reflect import autorun

Option = Select.Option


def picker_with_type(picker_type, onChange):
    if picker_type == "time":
        return TimePicker(onChange=onChange)
    if picker_type == "date":
        return DatePicker(onChange=onChange)
    return DatePicker(picker=picker_type, onChange=onChange)


def app():
    picker_type = Select(
        [
            Option("Time", value="time"),
            Option("Date", value="date"),
            Option("Week", value="week"),
            Option("Month", value="month"),
            Option("Quarter", value="quarter"),
            Option("Year", value="year"),
        ],
        defaultValue="time"
    )
    autorun(lambda: print(picker_type()))
    return Space(
        [
            picker_type,
            picker_with_type(picker_type=picker_type, onChange=print),
        ],
        direction="vertical",
    )
