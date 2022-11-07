from reflect_html import *
from reflect_antd import Result, Button


def app():
    return Result(
        "Go Console",
        status="success",
        title="Successfully Purchased Cloud Server ECS!",
        subTitle="Order number: 2017182818828182881 Cloud server configuration takes 1-5 minutes, please wait.",
        extra=[
            Button(type="primary", key="console"),
            Button("Buy Again", key="buy"),
        ],
    )
