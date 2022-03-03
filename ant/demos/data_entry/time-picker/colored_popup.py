from reflect_html import *
from reflect_antd import TimePicker

from reflect import autorun
from datetime import time


def app():
    time_picker = TimePicker(
        defaultValue=time(0, 0, 0),
        popupClassName="myCustomClassName",
    )
    autorun(lambda: print("changed", time_picker()))
    return time_picker