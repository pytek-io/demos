from reflect_html import *
from reflect_antd import TimePicker


def app():
    return TimePicker(minuteStep=15, secondStep=10)
