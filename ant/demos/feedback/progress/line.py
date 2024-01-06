import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Progress(percent=30),
            antd.Progress(percent=50, status="active"),
            antd.Progress(percent=70, status="exception"),
            antd.Progress(percent=100),
            antd.Progress(percent=50, showInfo=False),
        ]
    )
