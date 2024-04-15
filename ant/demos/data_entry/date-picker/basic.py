import datetime

import render as r
import render_antd as antd


def app(_):
    date_picker1 = antd.DatePicker(
        defaultValue=datetime.datetime.now() + datetime.timedelta(days=7)
    )
    return date_picker1
    # date_picker2 = antd.DatePicker(picker="week")
    # date_picker3 = antd.DatePicker(picker="month")
    # date_picker4 = antd.DatePicker(picker="quarter")
    # date_picker5 = antd.DatePicker(picker="year")
    # r.autorun(lambda: print("selected", date_picker1()))
    # r.autorun(lambda: print("selected", date_picker2()))
    # r.autorun(lambda: print("selected", date_picker3()))
    # r.autorun(lambda: print("selected", date_picker4()))
    # r.autorun(lambda: print("selected", date_picker5()))
    # return antd.Space(
    #     [date_picker1, date_picker2, date_picker3, date_picker4, date_picker5],
    #     direction="vertical",
    # )
