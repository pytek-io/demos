from reflect_html import *
from reflect_antd import Steps
from reflect_ant_icons import (
    UserOutlined,
    SolutionOutlined,
    LoadingOutlined,
    SmileOutlined,
)

Step = Steps.Step


def app():
    return Steps(
        [
            Step(status="finish", title="Login", icon=UserOutlined([])),
            Step(status="finish", title="Verification", icon=SolutionOutlined([])),
            Step(status="process", title="Pay", icon=LoadingOutlined([])),
            Step(status="wait", title="Done", icon=SmileOutlined([])),
        ]
    )
