import reflect_antd as antd
import reflect_html as html

Step = antd.Steps.Step


def app():
    size = antd.Radio.Group(
        [antd.Radio("Small", value="small"), antd.Radio("Default", value="default")],
        style=dict(marginBottom=16),
    )

    def horizontalSteps():
        antd.Card(
            antd.Steps(
                [
                    Step(title="Finished", description="This is a description."),
                    Step(title="In Progress", description="This is a description."),
                    Step(title="Waiting", description="This is a description."),
                ],
                size=size,
            )
        )

    return html.div(
        [
            size,
            antd.Steps(
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
