import reflect_antd as antd
import reflect_html as html
import reflect_ant_icons as ant_icons


def app():
    return html.div(
        [
            antd.FloatButton.Group(
                [
                    antd.FloatButton(),
                    antd.FloatButton(icon=ant_icons.QuestionCircleOutlined()),
                    antd.FloatButton(),
                    antd.FloatButton.BackTop(visibilityHeight=-1),
                ],
                shape="circle",
                style={"right": 24},
            ),
            antd.FloatButton.Group(
                [
                    antd.FloatButton(),
                    antd.FloatButton(icon=ant_icons.QuestionCircleOutlined()),
                    antd.FloatButton(),
                    antd.FloatButton(icon=ant_icons.SyncOutlined()),
                    antd.FloatButton.BackTop(visibilityHeight=-1),
                ],
                shape="square",
                style={"right": 94},
            ),
        ]
    )
