import reflect_antd as antd
import reflect_ant_icons as ant_icons


def app():
    return antd.FloatButton.Group(
        [antd.FloatButton(), antd.FloatButton(icon=ant_icons.CommentOutlined())],
        icon=ant_icons.CustomerServiceOutlined(),
        type="primary",
        trigger="click",
    )
