import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Progress(strokeLinecap="square", percent=75),
            antd.Progress(strokeLinecap="square", type="circle", percent=75),
            antd.Progress(strokeLinecap="square", type="dashboard", percent=75),
        ]
    )
