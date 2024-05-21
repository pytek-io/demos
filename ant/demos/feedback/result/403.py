import render_antd as antd


def app(_):
    return antd.Result(
        status="403",
        title="403",
        subTitle="Sorry, you are not authorized to access this page.",
        extra=antd.Button("Back Home", type="primary"),
    )
