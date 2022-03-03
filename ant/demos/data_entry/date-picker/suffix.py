from reflect_html import *
from reflect_antd import DatePicker, Space
from reflect_ant_icons import SmileOutlined

from reflect import autorun

RangePicker = DatePicker.RangePicker


def app():
    smileIcon = SmileOutlined()
    picker1 = DatePicker(suffixIcon=smileIcon)
    picker2 = DatePicker(suffixIcon=smileIcon, picker="month")
    picker3 = RangePicker(suffixIcon=smileIcon)
    picker4 = DatePicker(suffixIcon=smileIcon, picker="week")
    picker5 = DatePicker(suffixIcon="ab")
    picker6 = DatePicker(suffixIcon="ab", picker="month")
    picker7 = DatePicker(suffixIcon="ab")
    picker8 = DatePicker(suffixIcon="ab", picker="week")
    autorun(lambda: print("date picker1", picker1()))
    autorun(lambda: print("date picker2", picker2()))
    autorun(lambda: print("date picker3", picker3()))
    autorun(lambda: print("date picker4", picker4()))
    autorun(lambda: print("date picker5", picker5()))
    autorun(lambda: print("date picker6", picker6()))
    autorun(lambda: print("date picker7", picker7()))
    autorun(lambda: print("date picker8", picker8()))
    return Space(
        [
            picker1,
            picker2,
            picker3,
            picker4,
            picker5,
            picker6,
            picker7,
            picker8,
        ],
        direction="vertical",
        size=12,
    )
