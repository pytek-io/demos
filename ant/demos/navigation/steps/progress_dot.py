import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Steps(
                items=[
                    {"label": "Finished", "description": "This is a description."},
                    {"label": "In Progress", "description": "This is a description."},
                    {"label": "Waiting", "description": "This is a description."},
                ],
                progressDot=True,
                current=1,
            )
        ]
    )
