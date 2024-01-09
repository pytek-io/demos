import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.FloatButton.Group(
                [
                    antd.FloatButton(shape="circle", style={"right": 24}),
                    antd.FloatButton(
                        icon=ant_icons.QuestionCircleOutlined(),
                    ),
                    antd.FloatButton.BackTop(visibilityHeight=0),
                ],
                shape="circle",
                style={"right": 24},
            ),
            antd.FloatButton.Group(
                [
                    antd.FloatButton(shape="circle", style={"right": 24}),
                    antd.FloatButton(
                        icon=ant_icons.QuestionCircleOutlined(),
                    ),
                    antd.FloatButton(
                        icon=ant_icons.SyncOutlined(),
                    ),
                    antd.FloatButton.BackTop(visibilityHeight=0),
                ],
                shape="square",
                style={"right": 94},
            ),
        ]
    )
