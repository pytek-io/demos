import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            html.span(
                antd.Badge(
                    antd.Avatar(shape="square", icon=ant_icons.UserOutlined([])),
                    count=1,
                ),
                className="avatar-item",
            ),
            html.span(
                antd.Badge(
                    antd.Avatar(shape="square", icon=ant_icons.UserOutlined([])),
                    dot=True,
                )
            ),
        ]
    )
