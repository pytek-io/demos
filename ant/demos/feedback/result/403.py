from reflect_html import *
from reflect_antd import Result, Button


def app():
    return Result(
        "Back Home",
        status="403",
        title="403",
        subTitle="Sorry, you are not authorized to access this page.",
        extra=Button(type="primary"),
    )
