import reflect_antd as antd
import reflect_html as html
import reflect_ant_icons as ant_icons


def app():
    return html.div(
        [
            antd.FloatButton.Group(
                [
                    antd.FloatButton(icon=ant_icons.CommentOutlined()),
                ],
                trigger="click",
                type="primary",
                style={"right": 24},
                icon=ant_icons.CustomerServiceOutlined(),
            ),
            antd.FloatButton.Group(
                [
                    antd.FloatButton(icon=ant_icons.CommentOutlined()),
                ],
                trigger="hover",
                type="primary",
                style={"right": 94},
                icon=ant_icons.CustomerServiceOutlined(),
            ),
        ]
    )
