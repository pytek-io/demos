import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    icon = ant_icons.SmileOutlined()
    return html.div(
        [
            antd.Alert(icon=icon, message="showIcon = false", type="success"),
            antd.Alert(
                icon=icon, message="Success Tips", type="success", showIcon=True
            ),
            antd.Alert(
                icon=icon, message="Informational Notes", type="info", showIcon=True
            ),
            antd.Alert(icon=icon, message="Warning", type="warning", showIcon=True),
            antd.Alert(icon=icon, message="Error", type="error", showIcon=True),
            antd.Alert(
                icon=icon,
                message="Success Tips",
                description="Detailed description and advices about successful copywriting.",
                type="success",
                showIcon=True,
            ),
            antd.Alert(
                icon=icon,
                message="Informational Notes",
                description="Additional description and informations about copywriting.",
                type="info",
                showIcon=True,
            ),
            antd.Alert(
                icon=icon,
                message="Warning",
                description="This is a warning notice about copywriting.",
                type="warning",
                showIcon=True,
            ),
            antd.Alert(
                icon=icon,
                message="Error",
                description="This is an error message about copywriting.",
                type="error",
                showIcon=True,
            ),
        ]
    )
