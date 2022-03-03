from reflect_html import *
from reflect_antd import TimePicker

from reflect import autorun
from datetime import datetime


def app():
    time_picker1 = TimePicker(use12Hours=True, defaultValue=datetime.now())
    time_picker2 = TimePicker(
        use12Hours=True,
        format="h:mm:ss A",
        defaultValue=datetime.now(),
        style=dict(width=140),
    )
    time_picker3 = TimePicker(
        use12Hours=True, defaultValue=datetime.now(), format="h:mm a"
    )
    autorun(lambda: print("changed", time_picker1()))
    autorun(lambda: print("changed", time_picker1()))
    autorun(lambda: print("changed", time_picker2()))
    autorun(lambda: print("changed", time_picker3()))
    return div([time_picker1, time_picker2, time_picker3])
