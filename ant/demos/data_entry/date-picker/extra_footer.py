from reflect_html import *
from reflect_antd import DatePicker, Space
from reflect import js

RangePicker = DatePicker.RangePicker


def app():
    footer = lambda content: js("constant", content)
    return Space(
        [
            DatePicker(renderExtraFooter=footer("Select date XYZ")),
            DatePicker(renderExtraFooter=footer("Select time XYZ"), showTime=True),
            RangePicker(renderExtraFooter=footer("Select date range XYZ")),
            RangePicker(renderExtraFooter=footer("Select time XYZ"), showTime=True),
            DatePicker(renderExtraFooter=footer("Select month XYZ"), picker="month"),
        ],
        direction="vertical",
        size=12,
    )
