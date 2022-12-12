import reflect_antd as antd
import reflect_html as html
import reflect_ant_icons as ant_icons


def app():
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
