import reflect_antd as antd
import reflect_html as html


def app():
    size = antd.Radio.Group(
        [antd.Radio("Small", value="small"), antd.Radio("Default", value="default")],
        style={"marginBottom": 16},
    )

    def horizontalSteps():
        antd.Card(
            antd.Steps(
                items=[
                    {"title": "Finished", "description": "This is a description."},
                    {"title": "In Progress", "description": "This is a description."},
                    {"title": "Waiting", "description": "This is a description."},
                ],
                size=size,
            )
        )

    return html.div(
        [
            size,
            antd.Steps(
                items=[
                    {"title": "Finished", "description": horizontalSteps},
                    {"title": "In Progress", "description": "This is a description."},
                    {"title": "Waiting", "description": "This is a description."},
                ],
                size=size,
                direction="vertical",
            ),
        ]
    )
