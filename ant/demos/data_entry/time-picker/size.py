from reflect_html import *
from reflect_antd import TimePicker
from datetime import time


def app():
    return [
        TimePicker(defaultValue=time(12, 8, 23), size="large"),
        TimePicker(defaultValue=time(12, 8, 23)),
        TimePicker(defaultValue=time(12, 8, 23), size="small"),
    ]
