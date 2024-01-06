from render_html import *
from render_antd import Result, Button
from render_ant_icons import SmileOutlined


def app():
    return Result(
        "Next",
        icon=SmileOutlined(),
        title="Great, we have done all the operations!",
        extra=Button(type="primary"),
    )
