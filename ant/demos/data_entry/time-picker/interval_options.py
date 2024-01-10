import render_antd as antd
import render_html as html


def app(_):
    return antd.TimePicker(minuteStep=15, secondStep=10)
