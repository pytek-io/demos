import render_antd as antd


def app(_):
    return antd.Result(
        status="success",
        title="Successfully Purchased Cloud Server ECS!",
        subTitle="Order number: 2017182818828182881 Cloud server configuration takes 1-5 minutes, please wait.",
        extra=[
            antd.Button("Go Console", type="primary", key="console"),
            antd.Button("Buy Again", key="buy"),
        ],
    )
