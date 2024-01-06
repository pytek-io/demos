import render_antd as antd
import render_html as html


def app():
    return antd.Result(
        "Go Console",
        title="Your operation has been executed",
        extra=antd.Button(type="primary", key="console"),
    )
