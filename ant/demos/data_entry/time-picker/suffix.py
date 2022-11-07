import datetime

import reflect as r
import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    time_picker = antd.TimePicker(
        suffixIcon=ant_icons.SmileOutlined([]), defaultValue=datetime.time(0, 0, 0)
    )
    r.autorun(lambda: print(time_picker()))
    return time_picker
