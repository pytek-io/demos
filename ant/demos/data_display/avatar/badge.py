import reflect_ant_icons as ant_icons
import reflect_antd as antd


def app():
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
