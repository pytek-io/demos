from reflect_html import *
from reflect_antd import Steps, Divider
from reflect import make_observable, Callback

Step = Steps.Step


def app():
    current = make_observable(0)

    def onChange(value):
        print("onChange:", current)
        current.set(value)

    return [
        Steps(
            [
                Step(title="Step 1", description="This is a description."),
                Step(title="Step 2", description="This is a description."),
                Step(title="Step 3", description="This is a description."),
            ],
            current=current,
            onChange=Callback(onChange),
        ),
        Divider(),
        Steps(
            [
                Step(title="Step 1", description="This is a description."),
                Step(title="Step 2", description="This is a description."),
                Step(title="Step 3", description="This is a description."),
            ],
            current=current,
            onChange=Callback(onChange),
            direction="vertical",
        ),
    ]
