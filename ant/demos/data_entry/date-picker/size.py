from reflect_html import *
from reflect_antd import DatePicker, Radio, Space

RangePicker = DatePicker.RangePicker


def app():
    radio_group_size = Radio.Group(
        [
            Radio.Button("Large", value="large"),
            Radio.Button("Default", value="default"),
            Radio.Button("Small", value="small"),
        ],
    )
    return Space(
        [
            radio_group_size,
            DatePicker(size=radio_group_size),
            DatePicker(size=radio_group_size, picker="month"),
            RangePicker(size=radio_group_size),
            DatePicker(size=radio_group_size, picker="week"),
        ],
        direction="vertical",
        size=12,
    )