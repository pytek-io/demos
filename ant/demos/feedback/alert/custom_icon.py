from reflect_html import *
from reflect_antd import Alert
from reflect_ant_icons import SmileOutlined


def app():
    icon = SmileOutlined()
    return [
        Alert(icon=icon, message="showIcon = false", type="success"),
        Alert(icon=icon, message="Success Tips", type="success", showIcon=True),
        Alert(icon=icon, message="Informational Notes", type="info", showIcon=True),
        Alert(icon=icon, message="Warning", type="warning", showIcon=True),
        Alert(icon=icon, message="Error", type="error", showIcon=True),
        Alert(
            icon=icon,
            message="Success Tips",
            description="Detailed description and advices about successful copywriting.",
            type="success",
            showIcon=True,
        ),
        Alert(
            icon=icon,
            message="Informational Notes",
            description="Additional description and informations about copywriting.",
            type="info",
            showIcon=True,
        ),
        Alert(
            icon=icon,
            message="Warning",
            description="This is a warning notice about copywriting.",
            type="warning",
            showIcon=True,
        ),
        Alert(
            icon=icon,
            message="Error",
            description="This is an error message about copywriting.",
            type="error",
            showIcon=True,
        ),
    ]
