from reflect_html import *
from reflect_antd import Progress, Button
from reflect_ant_icons import MinusOutlined, PlusOutlined
from reflect import create_observable, autorun
from reflect_utils import increment_observable_bounded



def app():
    percent = create_observable(0)
    autorun(lambda: print("percent", percent()))
    return [
        Progress(type="circle", percent=percent),
        Button.Group(
            [
                Button(
                    onClick=increment_observable_bounded(percent, 0, 100, -10),
                    icon=MinusOutlined([]),
                ),
                Button(
                    onClick=increment_observable_bounded(percent, 0, 100, 10),
                    icon=PlusOutlined([]),
                ),
            ]
        ),
    ]
