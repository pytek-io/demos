from reflect_html import *
from reflect_antd import Tooltip, Progress


def app():
    return div(
        [
            Tooltip(
                Progress(percent=60, success=dict(percent=30)),
                title="3 done / 3 in progress / 4 to do",
            ),
            Tooltip(
                Progress(percent=60, success=dict(percent=30), type="circle"),
                title="3 done / 3 in progress / 4 to do",
            ),
            Tooltip(
                Progress(percent=60, success=dict(percent=30), type="dashboard"),
                title="3 done / 3 in progress / 4 to do",
            ),
        ]
    )
