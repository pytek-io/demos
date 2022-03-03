from reflect_html import *
from reflect_antd import Steps

Step = Steps.Step


def app():
    return Steps(
        [Step(title="Finished"), Step(title="In Progress"), Step(title="Waiting")],
        size="small",
        current=1,
    )
