from reflect_html import *
from reflect_antd import Progress


def app():
    return [
        Progress(strokeLinecap="square", percent=75),
        Progress(strokeLinecap="square", type="circle", percent=75),
        Progress(strokeLinecap="square", type="dashboard", percent=75),
    ]
