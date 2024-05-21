import render_antd as antd


def app(_):
    return antd.Result(
        title="Your operation has been executed",
        extra=antd.Button("Go Console", type="primary", key="console"),
    )
