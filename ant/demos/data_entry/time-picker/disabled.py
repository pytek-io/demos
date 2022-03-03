from reflect_html import *
from reflect_antd import TimePicker
from datetime import time


def app():
    return TimePicker(defaultValue=time(12, 8, 23), disabled=True)
