from reflect_html import *
from reflect_antd import Steps, Divider

Step = Steps.Step


def app():
    return div(
        [
            Steps(
                [
                    Step(title="Finished", description="This is a description."),
                    Step(title="In Progress", description="This is a description."),
                    Step(title="Waiting", description="This is a description."),
                ],
                progressDot=True,
                current=1,
            ),
            Divider(),
            Steps(
                [
                    Step(
                        title="Finished",
                        description="This is a description. This is a description.",
                    ),
                    Step(
                        title="Finished",
                        description="This is a description. This is a description.",
                    ),
                    Step(
                        title="In Progress",
                        description="This is a description. This is a description.",
                    ),
                    Step(title="Waiting", description="This is a description."),
                    Step(title="Waiting", description="This is a description."),
                ],
                progressDot=True,
                current=1,
                direction="vertical",
            ),
        ]
    )
