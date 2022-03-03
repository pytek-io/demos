from reflect_html import *
from reflect_antd import Progress


def app():
    return [
        Progress(type="dashboard", percent=75),
        Progress(type="dashboard", percent=75, gapDegree=30),
    ]
