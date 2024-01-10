import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Progress(type="circle", percent=75),
            antd.Progress(type="circle", percent=70, status="exception"),
            antd.Progress(type="circle", percent=100),
        ]
    )
