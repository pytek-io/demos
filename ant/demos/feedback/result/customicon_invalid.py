from reflect_html import *
from reflect_antd import Result, Button
from reflect_ant_icons import SmileOutlined


def app():
    return Result(
        "Next",
        icon=SmileOutlined(),
        title="Great, we have done all the operations!",
        extra=Button(type="primary"),
    )
