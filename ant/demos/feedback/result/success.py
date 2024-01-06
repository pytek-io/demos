import render_antd as antd
import render_html as html


def app():
    return antd.Result(
        "Go Console",
        status="success",
        title="Successfully Purchased Cloud Server ECS!",
        subTitle="Order number: 2017182818828182881 Cloud server configuration takes 1-5 minutes, please wait.",
        extra=[
            antd.Button(type="primary", key="console"),
            antd.Button("Buy Again", key="buy"),
        ],
    )
