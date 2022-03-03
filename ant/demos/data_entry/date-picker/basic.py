from reflect_html import *
from reflect_antd import DatePicker, Space

from datetime import datetime, timedelta
from reflect import autorun


def app():
    date_picker1 = DatePicker(defaultValue=datetime.now() + timedelta(days=7))
    date_picker2 = DatePicker(picker="week")
    date_picker3 = DatePicker(picker="month")
    date_picker4 = DatePicker(picker="quarter")
    date_picker5 = DatePicker(picker="year")
    autorun(lambda: print("selected", date_picker1()))
    autorun(lambda: print("selected", date_picker2()))
    autorun(lambda: print("selected", date_picker3()))
    autorun(lambda: print("selected", date_picker4()))
    autorun(lambda: print("selected", date_picker5()))

    return Space(
        [
            date_picker1,
            date_picker2,
            date_picker3,
            date_picker4,
            date_picker5,
        ],
        direction="vertical",
    )
