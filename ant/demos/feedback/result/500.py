import render_antd as antd
import render_html as html


def app(_):
    return antd.Result(
        "Back Home",
        status="500",
        title="500",
        subTitle="Sorry, something went wrong.",
        extra=antd.Button(type="primary"),
    )
