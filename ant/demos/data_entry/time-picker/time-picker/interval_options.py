import reflect_antd as antd
import reflect_html as html


def app():
    return antd.TimePicker(minuteStep=15, secondStep=10)
