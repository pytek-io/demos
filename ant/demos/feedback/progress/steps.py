from reflect_html import *
from reflect_antd import Progress


def app():
    return [
        Progress(percent=50, steps=3),
        br(),
        Progress(percent=30, steps=5),
        br(),
        Progress(percent=100, steps=5, size="small", strokeColor="#52c41a"),
    ]
