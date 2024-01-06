import render_antd as antd
import render_html as html


def app():
    return antd.Steps(
        items=[{"title": "Finished"}, {"title": "In Progress"}, {"title": "Waiting"}],
        size="small",
        current=1,
    )
