import render_antd as antd
import render_html as html


def app():
    return antd.Steps(
        items=[
            {"title": "Finished", "description": "This is a description."},
            {"title": "In Progress", "description": "This is a description."},
            {"title": "Waiting", "description": "This is a description."},
        ],
        direction="vertical",
        current=1,
    )
