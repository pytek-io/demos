from reflect_html import *
from reflect_antd import DatePicker, Space
from reflect import Callback
from reflect import autorun

RangePicker = DatePicker.RangePicker


def app():
    def onOk(value):
        print("onOk: ", value)

    def onChange(values):
        print("Selected Time: ", values)
        print(
            "Formatted Selected Time: ",
            [value.strftime("%Y-%M-%D %H:%m") for value in values],
        )

    date_picker = DatePicker(
        showTime=True,
        onOk=Callback(onOk),
    )
    range_picker = RangePicker(
        showTime=dict(format="HH:mm"),
        format="YYYY-MM-DD HH:mm",
        onChange=onChange,
        onOk=Callback(onOk),
    )

    autorun(lambda: print("date picker", date_picker()))
    autorun(lambda: print("range picker", range_picker()))
    return Space(
        [date_picker, range_picker],
        direction="vertical",
        size=12,
    )
