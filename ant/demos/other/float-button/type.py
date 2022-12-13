import reflect_antd as antd
import reflect_html as html
import reflect_ant_icons as ant_icons


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
