import render_antd as antd
import render_html as html

RangePicker = antd.DatePicker.RangePicker


def app():
    return antd.Space(
        [
            antd.DatePicker(bordered=False),
            antd.DatePicker(picker="week", bordered=False),
            antd.DatePicker(picker="month", bordered=False),
            antd.DatePicker(picker="year", bordered=False),
            RangePicker(bordered=False),
            RangePicker(picker="week", bordered=False),
            RangePicker(picker="month", bordered=False),
            RangePicker(picker="year", bordered=False),
        ],
        direction="vertical",
        size=12,
    )
