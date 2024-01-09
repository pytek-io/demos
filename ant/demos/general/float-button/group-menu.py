import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


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
