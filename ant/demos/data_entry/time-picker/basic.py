from datetime import time

from reflect import autorun
from reflect_antd import TimePicker
from reflect_html import *


def app():
    time_picker = TimePicker(
        defaultValue=time(0, 0, 0),
    )
    autorun(lambda: print("changed", time_picker()))
    return time_picker
