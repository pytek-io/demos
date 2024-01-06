import render_antd as antd
import render_html as html
import render_ant_icons as ant_icons


def app():
    return html.div(
        [
            antd.FloatButton(
                shape="square",
                icon=ant_icons.FileTextOutlined(),
                description="HELP INFO",
                style={"right": 24},
            ),
            antd.FloatButton(
                shape="square",
                description="HELP INFO",
                style={"right": 94},
            ),
            antd.FloatButton(
                shape="square",
                icon=ant_icons.FileTextOutlined(),
                description="HELP",
                style={"right": 164},
            ),
        ]
    )
