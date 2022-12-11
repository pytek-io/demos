import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Steps(
        items=[{"label": "Finished"}, {"label": "In Progress"}, {"label": "Waiting"}],
        size="small",
        current=1,
    )
