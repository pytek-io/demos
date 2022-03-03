from reflect_html import *
from reflect_antd import Steps

Step = Steps.Step


def app():
    return Steps(
        [
            Step(title="Finished", description="This is a description"),
            Step(title="In Process", description="This is a description"),
            Step(title="Waiting", description="This is a description"),
        ],
        current=1,
        status="error",
    )
