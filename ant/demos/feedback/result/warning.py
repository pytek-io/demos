import render_antd as antd


def app(_):
    return antd.Result(
        status="warning",
        title="There are some problems with your operation.",
        extra=antd.Button("Go Console", type="primary", key="console"),
    )
