import render_ant_icons as ant_icons
import render_antd as antd


def app(_):
    return antd.FloatButton.Group(
        [antd.FloatButton(), antd.FloatButton(icon=ant_icons.CommentOutlined())],
        icon=ant_icons.CustomerServiceOutlined(),
        type="primary",
        trigger="click",
    )
