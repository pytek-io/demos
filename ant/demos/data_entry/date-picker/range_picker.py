import render_antd as antd
import render_html as html

RangePicker = antd.DatePicker.RangePicker


def app(_):
    return antd.Space(
        [
            RangePicker(),
            RangePicker(showTime=True),
            RangePicker(picker="week"),
            RangePicker(picker="month"),
            RangePicker(picker="year"),
        ],
        direction="vertical",
        size=12,
    )
