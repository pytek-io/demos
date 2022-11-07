import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

Step = antd.Steps.Step


def app():
    return antd.Steps(
        [
            Step(status="finish", title="Login", icon=ant_icons.UserOutlined([])),
            Step(
                status="finish",
                title="Verification",
                icon=ant_icons.SolutionOutlined([]),
            ),
            Step(status="process", title="Pay", icon=ant_icons.LoadingOutlined([])),
            Step(status="wait", title="Done", icon=ant_icons.SmileOutlined([])),
        ]
    )
