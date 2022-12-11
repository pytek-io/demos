import reflect_antd as antd
import reflect_html as html


def app():
    size = antd.Radio.Group(
        [antd.Radio("Small", value="small"), antd.Radio("Default", value="default")],
        style=dict(marginBottom=16),
    )

    def horizontalSteps():
        antd.Card(
            antd.Steps(
                items=[
                    {"label": "Finished", "description": "This is a description."},
                    {"label": "In Progress", "description": "This is a description."},
                    {"label": "Waiting", "description": "This is a description."},
                ],
                size=size,
            )
        )

    return html.div(
        [
            size,
            antd.Steps(
                items=[
                    {"label": "Finished", "description": horizontalSteps},
                    {"label": "In Progress", "description": "This is a description."},
                    {"label": "Waiting", "description": "This is a description."},
                ],
                size=size,
                direction="vertical",
            ),
        ]
    )
