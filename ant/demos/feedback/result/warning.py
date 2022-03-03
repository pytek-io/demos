from reflect_html import *
from reflect_antd import Result, Button


def app():
    return Result(
        "Go Console",
        status="warning",
        title="There are some problems with your operation.",
        extra=Button(type="primary", key="console"),
    )
