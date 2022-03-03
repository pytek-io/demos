from reflect_html import *
from reflect_antd import Tooltip


def app():
    return Tooltip(
        span("Tooltip will destroy when hidden."),
        destroyTooltipOnHide=dict(keepParent=False),
        title="prompt text",
    )
