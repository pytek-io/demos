import render_antd as antd
import render_html as html


def app(_):
    return antd.Result(
        "Go Console",
        status="warning",
        title="There are some problems with your operation.",
        extra=antd.Button(type="primary", key="console"),
    )
