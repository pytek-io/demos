from render_ant_icons import SmileOutlined
from render_antd import Button, Result
from render_html import *


def app():
    return Result(
        "Next",
        icon=SmileOutlined(),
        title="Great, we have done all the operations!",
        extra=Button(type="primary"),
    )
