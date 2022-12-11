import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Steps(
        items=[
            {"label": "Finished", "description": "This is a description."},
            {"label": "In Progress", "description": "This is a description."},
            {"label": "Waiting", "description": "This is a description."},
        ],
        direction="vertical",
        size="small",
        current=1,
    )
