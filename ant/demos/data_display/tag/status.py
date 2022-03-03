from reflect_html import *
from reflect_antd import Tag, Divider


def app():
    return [
        Divider("Without icon", orientation="left"),
        div(
            [
                Tag("success", color="success"),
                Tag("processing", color="processing"),
                Tag("error", color="error"),
                Tag("warning", color="warning"),
                Tag("default", color="default"),
            ]
        ),
        Divider("With icon", orientation="left"),
        div(
            [
                Tag("success", icon=CheckCircleOutlined([]), color="success"),
                Tag("processing", icon=SyncOutlined(spin), color="processing"),
                Tag("error", icon=CloseCircleOutlined([]), color="error"),
                Tag("warning", icon=ExclamationCircleOutlined([]), color="warning"),
                Tag("waiting", icon=ClockCircleOutlined([]), color="default"),
                Tag("stop", icon=MinusCircleOutlined([]), color="default"),
            ]
        ),
    ]
