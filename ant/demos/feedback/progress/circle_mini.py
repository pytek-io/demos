import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Progress(type="circle", percent=30, width=80),
            antd.Progress(type="circle", percent=70, width=80, status="exception"),
            antd.Progress(type="circle", percent=100, width=80),
        ]
    )
