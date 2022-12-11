import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Steps(
        items=[
            {"label": "Finished", "description": "This is a description"},
            {"label": "In Process", "description": "This is a description"},
            {"label": "Waiting", "description": "This is a description"},
        ],
        current=1,
        status="error",
    )
