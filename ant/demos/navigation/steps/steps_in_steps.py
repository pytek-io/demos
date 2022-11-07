from reflect_html import *
from reflect_antd import Steps, Radio, Card

Step = Steps.Step


def app():
    size = Radio.Group(
        [Radio("Small", value="small"), Radio("Default", value="default")],
        style=dict(marginBottom=16),
    )

    def horizontalSteps():
        Card(
            Steps(
                [
                    Step(title="Finished", description="This is a description."),
                    Step(title="In Progress", description="This is a description."),
                    Step(title="Waiting", description="This is a description."),
                ],
                size=size,
            )
        )

    return div(
        [
            size,
            Steps(
                [
                    Step(title="Finished", description=horizontalSteps),
                    Step(title="In Progress", description="This is a description."),
                    Step(title="Waiting", description="This is a description."),
                ],
                size=size,
                direction="vertical",
            ),
        ]
    )
