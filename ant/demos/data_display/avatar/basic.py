import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            html.div(
                [
                    antd.Avatar(size=64, icon=ant_icons.UserOutlined([])),
                    antd.Avatar(size="large", icon=ant_icons.UserOutlined([])),
                    antd.Avatar(icon=ant_icons.UserOutlined([])),
                    antd.Avatar(size="small", icon=ant_icons.UserOutlined([])),
                ]
            ),
            html.div(
                [
                    antd.Avatar(
                        shape="square", size=64, icon=ant_icons.UserOutlined([])
                    ),
                    antd.Avatar(
                        shape="square", size="large", icon=ant_icons.UserOutlined([])
                    ),
                    antd.Avatar(shape="square", icon=ant_icons.UserOutlined([])),
                    antd.Avatar(
                        shape="square", size="small", icon=ant_icons.UserOutlined([])
                    ),
                ]
            ),
        ]
    )
