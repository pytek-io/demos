import reflect_antd as antd
import reflect_html as html

RangePicker = antd.DatePicker.RangePicker


def app():
    radio_group_size = antd.Radio.Group(
        [
            antd.Radio.Button("Large", value="large"),
            antd.Radio.Button("Default", value="default"),
            antd.Radio.Button("Small", value="small"),
        ]
    )
    return antd.Space(
        [
            radio_group_size,
            antd.DatePicker(size=radio_group_size),
            antd.DatePicker(size=radio_group_size, picker="month"),
            RangePicker(size=radio_group_size),
            antd.DatePicker(size=radio_group_size, picker="week"),
        ],
        direction="vertical",
        size=12,
    )
