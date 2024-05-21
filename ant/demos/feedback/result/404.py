import render_antd as antd


def app(_):
    return antd.Result(
        status="404",
        title="404",
        subTitle="Sorry, the page you visited does not exist.",
        extra=antd.Button("Back Home", type="primary"),
    )
