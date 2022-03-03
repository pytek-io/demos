from reflect_html import *
from reflect_antd import Result, Button


def app():
    return Result(
        "Go Console",
        title="Your operation has been executed",
        extra=Button(type="primary", key="console"),
    )
