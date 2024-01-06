import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.FloatButton(
                icon=ant_icons.QuestionCircleOutlined(),
                type="primary",
                style={"right": 24},
            ),
            antd.FloatButton(
                icon=ant_icons.QuestionCircleOutlined(),
                type="default",
                style={"right": 94},
            ),
        ]
    )
