import render_antd as antd
import render_html as html


def app(_):
    return antd.Steps(
        items=[
            {"title": "Finished", "description": "This is a description."},
            {"title": "In Progress", "description": "This is a description."},
            {"title": "Waiting", "description": "This is a description."},
        ],
        direction="vertical",
        size="small",
        current=1,
    )
