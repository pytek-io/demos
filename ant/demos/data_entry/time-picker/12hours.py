import datetime

import render as r
import render_antd as antd
import render_html as html


def app():
    time_picker1 = antd.TimePicker(
        use12Hours=True, defaultValue=datetime.datetime.now()
    )
    time_picker2 = antd.TimePicker(
        use12Hours=True,
        format="h:mm:ss A",
        defaultValue=datetime.datetime.now(),
        style={"width": 140},
    )
    time_picker3 = antd.TimePicker(
        use12Hours=True, defaultValue=datetime.datetime.now(), format="h:mm a"
    )
    r.autorun(lambda: print("changed", time_picker1()))
    r.autorun(lambda: print("changed", time_picker1()))
    r.autorun(lambda: print("changed", time_picker2()))
    r.autorun(lambda: print("changed", time_picker3()))
    return html.div([time_picker1, time_picker2, time_picker3])
