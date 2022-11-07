from reflect_html import *
from reflect_antd import Progress


def app():
    return div(
        [
            Progress(percent=30),
            Progress(percent=50, status="active"),
            Progress(percent=70, status="exception"),
            Progress(percent=100),
            Progress(percent=50, showInfo=False),
        ]
    )
