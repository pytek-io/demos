from reflect_html import *
from reflect_antd import Result, Button


def app():
    return Result(
        "Back Home",
        status="500",
        title="500",
        subTitle="Sorry, something went wrong.",
        extra=Button(type="primary"),
    )
