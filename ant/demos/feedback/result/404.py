from reflect_html import *
from reflect_antd import Result, Button


def app():
    return Result(
        "Back Home",
        status="404",
        title="404",
        subTitle="Sorry, the page you visited does not exist.",
        extra=Button(type="primary"),
    )
