import datetime

import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app(_):
    time_picker = antd.TimePicker(
        suffixIcon=ant_icons.SmileOutlined([]), defaultValue=datetime.time(0, 0, 0)
    )
    r.autorun(lambda: print(time_picker()))
    return time_picker
