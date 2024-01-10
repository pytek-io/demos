import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.FloatButton(
                icon=ant_icons.FileTextOutlined(),
                description="HELP INFO",
                shape="square",
                style={"right": 24},
            ),
            antd.FloatButton(
                description="HELP INFO", shape="square", style={"right": 94}
            ),
            antd.FloatButton(
                icon=ant_icons.FileTextOutlined(),
                description="HELP",
                shape="square",
                style={"right": 164},
            ),
        ]
    )
