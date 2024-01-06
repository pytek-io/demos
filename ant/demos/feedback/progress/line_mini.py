import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Progress(percent=30, size="small"),
            antd.Progress(percent=50, size="small", status="active"),
            antd.Progress(percent=70, size="small", status="exception"),
            antd.Progress(percent=100, size="small"),
        ],
        style={"width": 170},
    )
