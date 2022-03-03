from reflect_html import *
from reflect_antd import Progress


def app():
    return div(
        [
            Progress(percent=30, size="small"),
            Progress(percent=50, size="small", status="active"),
            Progress(percent=70, size="small", status="exception"),
            Progress(percent=100, size="small"),
        ],
        style=dict(width=170),
    )
