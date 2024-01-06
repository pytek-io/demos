import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app():
    return antd.Steps(
        items=[
            {"status": "finish", "title": "Login", "icon": ant_icons.UserOutlined([])},
            {
                "status": "finish",
                "title": "Verification",
                "icon": ant_icons.SolutionOutlined([]),
            },
            {
                "status": "process",
                "title": "Pay",
                "icon": ant_icons.LoadingOutlined([]),
            },
            {"status": "wait", "title": "Done", "icon": ant_icons.SmileOutlined([])},
        ]
    )
