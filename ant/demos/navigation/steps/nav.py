from reflect_html import *
from reflect_antd import Steps
from reflect import Callback
from reflect import create_observable

Step = Steps.Step


def app():

    current = create_observable(0)

    def onChange(current_value):
        print("onChange:", current_value)
        current.set(current_value)

    return div([
        Steps(
            [
                Step(
                    title="Step 1",
                    subTitle="00:00:05",
                    status="finish",
                    description="This is a description.",
                ),
                Step(
                    title="Step 2",
                    subTitle="00:01:02",
                    status="process",
                    description="This is a description.",
                ),
                Step(
                    title="Step 3",
                    subTitle="waiting for longlong time",
                    status="wait",
                    description="This is a description.",
                ),
            ],
            type="navigation",
            size="small",
            current=current,
            onChange=Callback(onChange),
            className="site-navigation-steps",
        ),
        Steps(
            [
                Step(status="finish", title="Step 1"),
                Step(status="process", title="Step 2"),
                Step(status="wait", title="Step 3"),
                Step(status="wait", title="Step 4"),
            ],
            type="navigation",
            current=current,
            onChange=Callback(onChange),
            className="site-navigation-steps",
        ),
        Steps(
            [
                Step(status="finish", title="finish 1"),
                Step(status="finish", title="finish 2"),
                Step(status="process", title="current process"),
                Step(status="wait", title="wait", disabled=True),
            ],
            type="navigation",
            size="small",
            current=current,
            onChange=Callback(onChange),
            className="site-navigation-steps",
        ),
    ]
)