import render_ant_icons as ant_icons
import render_antd as antd


def app(_):
    return antd.Space(
        [
            antd.Badge(
                antd.Avatar(shape="square", icon=ant_icons.UserOutlined([])),
                count=1,
            ),
            antd.Badge(
                antd.Avatar(shape="square", icon=ant_icons.UserOutlined([])),
                dot=True,
            ),
        ]
    )
