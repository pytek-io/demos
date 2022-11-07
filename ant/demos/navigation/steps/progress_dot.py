import reflect_antd as antd
import reflect_html as html

Step = antd.Steps.Step


def app():
    return html.div(
        [
            antd.Steps(
                [
                    Step(title="Finished", description="This is a description."),
                    Step(title="In Progress", description="This is a description."),
                    Step(title="Waiting", description="This is a description."),
                ],
                progressDot=True,
                current=1,
            ),
            antd.Divider(),
            antd.Steps(
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
