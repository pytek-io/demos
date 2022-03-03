from reflect_html import *
from reflect_antd import Alert


def app():
    return [
        Alert(message="Success Tips", type="success", showIcon=True),
        Alert(message="Informational Notes", type="info", showIcon=True),
        Alert(message="Warning", type="warning", showIcon=True, closable=True),
        Alert(message="Error", type="error", showIcon=True),
        Alert(
            message="Success Tips",
            description="Detailed description and advice about successful copywriting.",
            type="success",
            showIcon=True,
        ),
        Alert(
            message="Informational Notes",
            description="Additional description and information about copywriting.",
            type="info",
            showIcon=True,
        ),
        Alert(
            message="Warning",
            description="This is a warning notice about copywriting.",
            type="warning",
            showIcon=True,
            closable=True,
        ),
        Alert(
            message="Error",
            description="This is an error message about copywriting.",
            type="error",
            showIcon=True,
        ),
    ]
