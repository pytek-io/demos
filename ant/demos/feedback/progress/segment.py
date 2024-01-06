import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Tooltip(
                antd.Progress(percent=60, success={"percent": 30}),
                title="3 done / 3 in progress / 4 to do",
            ),
            antd.Tooltip(
                antd.Progress(percent=60, success={"percent": 30}, type="circle"),
                title="3 done / 3 in progress / 4 to do",
            ),
            antd.Tooltip(
                antd.Progress(percent=60, success={"percent": 30}, type="dashboard"),
                title="3 done / 3 in progress / 4 to do",
            ),
        ]
    )
