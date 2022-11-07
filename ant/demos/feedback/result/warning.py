import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Result(
        "Go Console",
        status="warning",
        title="There are some problems with your operation.",
        extra=antd.Button(type="primary", key="console"),
    )
