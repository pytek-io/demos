import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Steps(
        items=[
            {"status": "finish", "label": "Login", "icon": ant_icons.UserOutlined([])},
            {
                "status": "finish",
                "label": "Verification",
                "icon": ant_icons.SolutionOutlined([]),
            },
            {
                "status": "process",
                "label": "Pay",
                "icon": ant_icons.LoadingOutlined([]),
            },
            {"status": "wait", "label": "Done", "icon": ant_icons.SmileOutlined([])},
        ]
    )
