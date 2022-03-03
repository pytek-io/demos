from reflect_html import *
from reflect_antd import TimePicker

from reflect import autorun
from datetime import time


def app():
    time_picker = TimePicker(
        defaultValue=time(0, 0, 0),
    )
    autorun(lambda: print(time_picker()))
    return time_picker
