import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Steps(
                items=[
                    {"title": "Finished", "description": "This is a description."},
                    {"title": "In Progress", "description": "This is a description."},
                    {"title": "Waiting", "description": "This is a description."},
                ],
                progressDot=True,
                current=1,
            )
        ]
    )
