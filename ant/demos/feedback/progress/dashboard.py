import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Progress(type="dashboard", percent=75),
            antd.Progress(type="dashboard", percent=75, gapDegree=30),
        ]
    )
