import render_antd as antd
import render_html as html


def app(_):
    return antd.Result(
        status="500",
        title="500",
        subTitle="Sorry, something went wrong.",
        extra=antd.Button("Back Home", type="primary"),
    )
