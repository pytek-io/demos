import render_antd as antd
import render_html as html

RangePicker = antd.TimePicker.RangePicker


def app():
    return RangePicker()
