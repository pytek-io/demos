from reflect_html import *
from reflect_antd import Progress


def app():
    return div(
        [
            Progress(type="circle", percent=75),
            Progress(type="circle", percent=70, status="exception"),
            Progress(type="circle", percent=100),
        ]
    )
