import render_antd as antd
import render_html as html


def app():
    return antd.Result(
        "Back Home",
        status="403",
        title="403",
        subTitle="Sorry, you are not authorized to access this page.",
        extra=antd.Button(type="primary"),
    )
