from reflect_html import *
from reflect_antd import TimePicker
from reflect_ant_icons import SmileOutlined

from reflect import autorun
from datetime import time


def app():
    time_picker = TimePicker(
        suffixIcon=SmileOutlined([]),
        defaultValue=time(0, 0, 0),
    )
    autorun(lambda: print(time_picker()))
    return time_picker