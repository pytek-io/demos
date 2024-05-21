import datetime

import render as r
import render_antd as antd


def app(_):
    date_picker1 = antd.DatePicker(
        defaultValue=datetime.datetime.now() + datetime.timedelta(days=7)
    )
    return date_picker1
